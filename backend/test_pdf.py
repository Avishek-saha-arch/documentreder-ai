from services.pdf_service import convert_pdf_to_images

images = convert_pdf_to_images("uploads/153023d9-83f5-4730-83fa-756d26a386c1.pdf")

print(images)