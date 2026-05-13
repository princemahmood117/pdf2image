# PDF to Image Conversion (Using pdf2image)

## Overview
This script converts selected pages from a PDF file into image files (JPEG format). It is useful when you want to extract a specific range of pages from a PDF and save them as individual images for previewing, processing, or sharing.

## How It Works

The program reads a PDF file and extracts only a defined range of pages. Those pages are then rendered as images using a PDF rendering backend (Poppler via `pdf2image`). After conversion, each page is saved separately as a JPEG image inside a local folder.

## Process Flow

1. The PDF file is loaded from the given path.
2. A specific page range (from page 27 to 46) is selected instead of converting the entire document.
3. Each selected page is converted into an image object in memory.
4. The images are iterated over and saved one by one as `.jpg` files in the `image` directory.
5. The saved images are named sequentially based on their order in the extracted range.

## Output
- A set of JPEG images representing pages 27–46 of the PDF.
- Files are stored locally in the `./image/` directory with sequential naming.

## Use Cases
- Converting book chapters into images
- Extracting report sections for sharing
- Preprocessing PDFs for computer vision or OCR tasks
- Creating previews of selected PDF sections