from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
    NLTKTextSplitter,
    HTMLHeaderTextSplitter,
    MarkdownHeaderTextSplitter
)
import pandas as pd
import fitz
import nltk
nltk.download('punkt_tab')

doc = fitz.open("resume.pdf")
text = ""

for page in doc:
    text += page.get_text()

text += """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Technical Skills Overview</title>
            
        </head>
        <body>

            <h1>Technical Skills Overview</h1>

            <table>
                <tr>
                    <th>Programming Languages & Frameworks</th>
                    <td>Java, J2EE, Spring (Spring Framework), React JS, Express JS</td>
                </tr>
                <tr>
                    <th>Architecture & Design</th>
                    <td>Microservices Architecture, RDBMS (Relational Database Management Systems), NoSQL (Hands-on experience)</td>
                </tr>
                <tr>
                    <th>Messaging & Integration</th>
                    <td>Kafka (Event Streaming Platform)</td>
                </tr>
                <tr>
                    <th>Containerization & Deployment</th>
                    <td>Docker (Containerization Platform)</td>
                </tr>
                <tr>
                    <th>DevOps & Continuous Delivery</th>
                    <td>CI/CD (Continuous Integration / Continuous Deployment)</td>
                </tr>
                <tr>
                    <th>Cloud Technology</th>
                    <td>Hands-on experiences on AWS, Azure</td>
                </tr>
                <tr>
                    <th>AI/ML</th>
                    <td>LLMs Integration (Hands-on experience with Gemini / ChatGPT)</td>
                </tr>
            </table>
 
        </body>
        </html>

        """

splitters = {
    "Recursive": RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20),
    "Character": CharacterTextSplitter(chunk_size=100, chunk_overlap=20, separator=" "),
    "Token": TokenTextSplitter(chunk_size=100, chunk_overlap=20),
    "NLTK": NLTKTextSplitter(chunk_size=100, chunk_overlap=20),
    "HTML": HTMLHeaderTextSplitter(headers_to_split_on=[("h1", "Header 1")]),
    "MARKDOWN": MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1")])
}

results = {}

for name, splitter in splitters.items():
    chunks = splitter.split_text(text)
    results[name] = chunks

data = []

for name, chunks in results.items():
    for i, chunk in enumerate(chunks):
        info = {
            "method": name,
            "chunkNo #": i + 1
        }
        if name in ['HTML', 'MARKDOWN']:
            info["length"] = len(chunk.page_content)
            info["content "]= chunk.page_content
        else:
            info["length"]= len(chunk)
            info["content"] = chunk.strip()

        data.append(info)

df = pd.DataFrame(data)
df.to_csv("chunk_analysis.csv", index=False)
df.to_json("chunk_analysis.json", orient="records", indent=2)