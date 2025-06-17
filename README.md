# chirag-hobby-projects
This repo contains hobby projects and utility functions.

## PDF Trimming Utility

`pdf_trim.py` provides a simple command line tool to extract a range of pages from a PDF file and save the result in a preset directory (`trimmed_pdfs` by default).

### Usage

```bash
python pdf_trim.py path/to/file.pdf START_PAGE END_PAGE [--output-dir OUTPUT_DIR]
```

Example:

```bash
python pdf_trim.py sample.pdf 2 5 --output-dir output
```

This will create `output/sample.pdf` containing only pages 2 through 5.
