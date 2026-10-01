#!/usr/bin/env python3
"""
PDF to DOCX Converter
High-fidelity PDF to Microsoft Word (.docx) document conversion tool.
Preserves text formatting, fonts, layouts, images, and tables.
"""

import argparse
import os
import sys
import time
import warnings

# Suppress PyMuPDF deprecation warning from pdf2docx
warnings.filterwarnings("ignore", category=UserWarning, module="fitz")
warnings.filterwarnings("ignore", message=".*The `fitz` API is deprecated.*")

try:
    import pymupdf
    # Alias fitz to pymupdf before pdf2docx imports fitz to suppress deprecation notice
    sys.modules["fitz"] = pymupdf
    from pdf2docx import Converter
except ImportError:
    print(
        "Error: Required packages not installed.\n"
        "Please install requirements using: pip install -r requirements.txt\n"
        "Or use the project's virtualenv: ./.venv/bin/python pdf_to_docx.py",
        file=sys.stderr,
    )
    sys.exit(1)


def parse_page_range(pages_str: str, max_pages: int) -> list[int]:
    """
    Parses a page range string like "1-5,8,11-15" (1-indexed) into a list of 0-indexed page indices.
    """
    indices = set()
    parts = [p.strip() for p in pages_str.split(",") if p.strip()]
    for part in parts:
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s.strip())
            end = int(end_s.strip())
            if start < 1:
                start = 1
            if end > max_pages:
                end = max_pages
            for p in range(start, end + 1):
                indices.add(p - 1)
        else:
            p = int(part)
            if 1 <= p <= max_pages:
                indices.add(p - 1)
    return sorted(list(indices))


def print_pdf_info(pdf_path: str):
    """
    Prints structural information and metadata of the PDF document.
    """
    import pymupdf

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    metadata = doc.metadata or {}

    print("=" * 60)
    print(f" PDF Document Information: {os.path.basename(pdf_path)}")
    print("=" * 60)
    print(f"File Path:   {os.path.abspath(pdf_path)}")
    print(f"File Size:   {os.path.getsize(pdf_path) / (1024 * 1024):.2f} MB")
    print(f"Page Count:  {total_pages}")
    print(f"Title:       {metadata.get('title') or 'N/A'}")
    print(f"Author:      {metadata.get('author') or 'N/A'}")
    print(f"Creator:     {metadata.get('creator') or 'N/A'}")
    print(f"Producer:    {metadata.get('producer') or 'N/A'}")
    print(f"Format:      {metadata.get('format') or 'N/A'}")

    # Inspect bookmarks / Table of Contents if available
    toc = doc.get_toc()
    if toc:
        print(f"\nBookmarks / Table of Contents ({len(toc)} entries found):")
        for lvl, title, page in toc[:15]:
            indent = "  " * (lvl - 1)
            print(f"{indent}- {title} (page {page})")
        if len(toc) > 15:
            print(f"  ... and {len(toc) - 15} more entries")
    else:
        print("\nBookmarks / Table of Contents: None embedded")

    print("=" * 60)
    doc.close()


def convert_pdf_to_docx(
    pdf_path: str,
    docx_path: str = None,
    start_page: int = None,
    end_page: int = None,
    pages: str = None,
    multi_processing: bool = True,
    cpu_count: int = None,
) -> str:
    """
    Converts a PDF file to DOCX.

    Parameters:
    - pdf_path: Path to the input PDF file.
    - docx_path: Destination path for the DOCX output (defaults to same folder/base name).
    - start_page: 1-indexed starting page number.
    - end_page: 1-indexed ending page number (inclusive).
    - pages: Page range string (e.g. '1-10,15,20-25').
    - multi_processing: Whether to use multi-core processing for acceleration.
    - cpu_count: Number of worker CPU cores.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    import pymupdf

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    doc.close()

    if not docx_path:
        base_name, _ = os.path.splitext(pdf_path)
        docx_path = f"{base_name}.docx"

    # Determine pages / range
    zero_based_pages = None
    start_idx = 0
    end_idx = total_pages

    if pages:
        zero_based_pages = parse_page_range(pages, total_pages)
        pages_to_convert_count = len(zero_based_pages)
        page_info_str = f"Specific pages: {pages} ({pages_to_convert_count} pages)"
    else:
        if start_page is not None:
            start_idx = max(0, start_page - 1)
        if end_page is not None:
            end_idx = min(total_pages, end_page)
        pages_to_convert_count = end_idx - start_idx
        page_info_str = f"Pages {start_idx + 1} to {end_idx} (total {pages_to_convert_count} pages)"

    if pages_to_convert_count <= 0:
        raise ValueError("No valid pages selected for conversion.")

    # Determine CPU workers
    available_cpus = os.cpu_count() or 1
    if cpu_count is None:
        cpu_count = min(available_cpus, 8) if multi_processing and pages_to_convert_count > 3 else 1

    use_mp = multi_processing and cpu_count > 1 and pages_to_convert_count > 3

    print("-" * 60)
    print("Starting PDF to DOCX Conversion")
    print(f"Input:       {pdf_path}")
    print(f"Output:      {docx_path}")
    print(f"Selection:   {page_info_str}")
    print(f"Parallel:    {'Yes (workers=' + str(cpu_count) + ')' if use_mp else 'No (single-thread)'}")
    print("-" * 60)

    start_time = time.time()

    cv = Converter(pdf_path)
    try:
        if zero_based_pages is not None:
            cv.convert(
                docx_path,
                pages=zero_based_pages,
                multi_processing=use_mp,
                cpu_count=cpu_count if use_mp else None,
            )
        else:
            cv.convert(
                docx_path,
                start=start_idx,
                end=end_idx,
                multi_processing=use_mp,
                cpu_count=cpu_count if use_mp else None,
            )
    finally:
        cv.close()

    elapsed = time.time() - start_time
    output_size_mb = os.path.getsize(docx_path) / (1024 * 1024)
    speed = pages_to_convert_count / elapsed if elapsed > 0 else 0

    print("-" * 60)
    print("Conversion completed successfully!")
    print(f"Saved file:  {docx_path} ({output_size_mb:.2f} MB)")
    print(f"Time taken:  {elapsed:.2f}s ({speed:.2f} pages/sec)")
    print("-" * 60)

    return docx_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to high-fidelity Microsoft Word (.docx) documents."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="documents/Introdução ao Santos Ministério.pdf",
        help="Path to input PDF file (default: documents/Introdução ao Santos Ministério.pdf)",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=None,
        help="Path to output DOCX file (default: same name with .docx extension)",
    )
    parser.add_argument(
        "-i", "--info",
        action="store_true",
        help="Display PDF information and table of contents without converting",
    )
    parser.add_argument(
        "-s", "--start",
        type=int,
        default=None,
        help="1-indexed starting page number",
    )
    parser.add_argument(
        "-e", "--end",
        type=int,
        default=None,
        help="1-indexed ending page number (inclusive)",
    )
    parser.add_argument(
        "-p", "--pages",
        type=str,
        default=None,
        help="Page specification (e.g. '1-10', '1,3,5-8', or '11-30')",
    )
    parser.add_argument(
        "--no-parallel",
        action="store_true",
        help="Disable multi-core processing",
    )
    parser.add_argument(
        "-c", "--cpu-count",
        type=int,
        default=None,
        help="Number of CPU cores for parallel conversion",
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file does not exist: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.info:
        print_pdf_info(args.input)
        return

    try:
        convert_pdf_to_docx(
            pdf_path=args.input,
            docx_path=args.output,
            start_page=args.start,
            end_page=args.end,
            pages=args.pages,
            multi_processing=not args.no_parallel,
            cpu_count=args.cpu_count,
        )
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
