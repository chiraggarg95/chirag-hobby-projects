import os
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
    """Prompt the user for input and trim the PDF."""
    pdf_path = input("Enter the path to the PDF file: ").strip()
    start_page = int(input("Enter the start page number (1-indexed): "))
    end_page = int(input("Enter the end page number (inclusive, 1-indexed): "))
    output_dir = input("Output directory [trimmed_pdfs]: ").strip() or "trimmed_pdfs"

    output = trim_pdf(pdf_path, start_page, end_page, output_dir)
    print(f"Trimmed PDF saved to: {output}")


if __name__ == "__main__":
    main()
