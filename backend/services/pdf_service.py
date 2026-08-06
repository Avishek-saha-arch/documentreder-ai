import fitz
from pathlib import Path


def convert_pdf_to_images(pdf_path: str):

    pdf = fitz.open(pdf_path)

    image_paths = []

    output_folder = Path("temp_images")
    output_folder.mkdir(exist_ok=True)

    for page_number in range(len(pdf)):

        page = pdf.load_page(page_number)

        pix = page.get_pixmap(dpi=200)

        image_path = output_folder / f"page_{page_number + 1}.png"

        pix.save(str(image_path))

        image_paths.append(str(image_path))

    pdf.close()

    return image_paths