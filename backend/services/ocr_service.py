import os

os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"

from paddleocr import PaddleOCR

# Load the OCR model once when the application starts
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    lang="en"
)


def extract_text(image_path):
    """
    Reads text from an image using PaddleOCR.
    Returns the extracted text as a single string.
    """

    result = ocr.predict(image_path)

    lines = []

    for page in result:
        if "rec_texts" in page:
            lines.extend(page["rec_texts"])

    return "\n".join(lines)