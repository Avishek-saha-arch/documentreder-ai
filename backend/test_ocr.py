from services.ocr_service import extract_text

text = extract_text("temp_images/page_1.png")

print("\n========== OCR RESULT ==========\n")
print(text)
print("\n===============================\n")