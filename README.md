# Document Chuncking Analysis

This code is for analyzing different text splitting methods using LangChain's text splitters on PDF documents and HTML content.

## Overview

This tool extracts text from a PDF resume, appends HTML content containing technical skills information, and then applies various text splitting strategies to analyze how different methods chunk the content. The results are saved in both CSV and JSON formats for further analysis.

## Features

- **PDF Text Extraction**: Extracts text from PDF documents using PyMuPDF
- **Multiple Text Splitting Methods**: Implements 6 different text splitting strategies
- **HTML Content Integration**: Appends structured HTML content to demonstrate splitting on mixed content types
- **Comprehensive Analysis**: Generates detailed chunk analysis with metadata
- **Multiple Output Formats**: Exports results to both CSV and JSON

## Text Splitting Methods

The tool evaluates the following LangChain text splitters:

1. **Recursive Character Text Splitter**: Splits text recursively by different characters
2. **Character Text Splitter**: Splits text by a specified separator (space)
3. **Token Text Splitter**: Splits text based on token count
4. **NLTK Text Splitter**: Uses NLTK for sentence-aware splitting
5. **HTML Header Text Splitter**: Splits HTML content by header tags
6. **Markdown Header Text Splitter**: Splits Markdown content by header levels

## Requirements

```python
langchain
pandas
PyMuPDF (fitz)
nltk
```

## Installation

```bash
pip install langchain pandas PyMuPDF nltk
```

## Usage

1. **Place your PDF file**: Ensure `resume.pdf` is in the same directory as the script
2. **Run the script**: Execute the Python file
3. **View results**: Check the generated `chunk_analysis.csv` and `chunk_analysis.json` files

```bash
python text_splitter_analysis.py
```

## Configuration

### Chunk Parameters (Default, can be changed)

- **Chunk Size**: 100 characters
- **Chunk Overlap**: 20 characters
- **Character Separator**: Space (" ")

### HTML Header Splitting (Default, can be changed)

- **Headers to Split**: H1 tags (`<h1>`)

### Markdown Header Splitting (Default, can be changed)

- **Headers to Split**: Level 1 headers (`#`)

## Output Structure

### CSV/JSON Fields

- `method`: Name of the splitting method used
- `chunkNo #`: Sequential chunk number
- `length`: Character count of the chunk
- `content`: The actual text content of the chunk

### Special Handling

- HTML and Markdown splitters return document objects with `page_content` attribute
- Other splitters return plain text strings
- All content is stripped of leading/trailing whitespace

## File Outputs

- **`chunk_analysis.csv`**: Tabular format for spreadsheet analysis
- **`chunk_analysis.json`**: JSON format with proper indentation for programmatic use

## Use Cases

- **Document Processing Pipeline Design**: Compare splitting methods for your specific content type
- **RAG System Optimization**: Evaluate which splitting strategy works best for retrieval
- **Content Analysis**: Understand how different methods handle mixed content (PDF + HTML)
- **Performance Benchmarking**: Analyze chunk sizes and distributions across methods

## Analysis Notes for Identifying Optimal Chunking Strategy

- Check how many chunks get created from a single segment.
- Look at the length of the chunks — the length should stay consistent throughout.
- Make sure the chunked statements still make sense and carry meaning.
- Try changing the chunking method and overlap settings to see which approach gives the most meaningful segments.
- For token-based chunking, see how many tokens are generated from a given amount of data. If simple information uses too many tokens, it might be worth exploring other options.
- Check how well the chunking strategy handles different data types like HTML, Markdown, images, and so on.

## Customization

You can modify the following parameters:

- **Chunk size and overlap**: Adjust in the splitters dictionary
- **PDF filename**: Change `"resume.pdf"` to your target file
- **HTML content**: Modify the embedded HTML string
- **Output filenames**: Change CSV and JSON output names
- **Splitting headers**: Modify headers_to_split_on for HTML/Markdown splitters
