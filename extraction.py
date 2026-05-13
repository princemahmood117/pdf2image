from pdf2image import convert_from_path

images = convert_from_path(
    './book.pdf',
    first_page=27,
    last_page=46,
    # poppler_path=r"../../../Downloads/Compressed/Release-25.12.0-0/Library/bin"
)

for i, img in enumerate(images):
    img.save(f'./image/page_{i+1}.jpg', 'JPEG')