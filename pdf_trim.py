import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def trim_pdf(source_path: str, start_page: int, end_page: int, output_dir: str = "trimmed_pdfs") -> str:
    """Trim a PDF from start_page to end_page (inclusive) and save it.

    Args:
        source_path: Path to the source PDF file.
        start_page: 1-indexed start page.
        end_page: 1-indexed end page.
        output_dir: Directory where the trimmed PDF will be saved.

    Returns:
        Path to the trimmed PDF.
    """
    if start_page < 1 or end_page < start_page:
        raise ValueError("Invalid page range")

    reader = PdfReader(source_path)
    num_pages = len(reader.pages)

    start_index = start_page - 1
    end_index = min(end_page, num_pages)

    writer = PdfWriter()
    for page_num in range(start_index, end_index):
        writer.add_page(reader.pages[page_num])

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(source_path))
    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Trim pages from a PDF file")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("start_page", type=int, help="Start page number (1-indexed)")
    parser.add_argument("end_page", type=int, help="End page number (inclusive, 1-indexed)")
    parser.add_argument("--output-dir", default="trimmed_pdfs", help="Directory to save the trimmed PDF")
    args = parser.parse_args()

    output = trim_pdf(args.pdf_path, args.start_page, args.end_page, args.output_dir)
    print(f"Trimmed PDF saved to: {output}")


if __name__ == "__main__":
    main()
