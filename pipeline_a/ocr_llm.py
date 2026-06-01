import json
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")


def extract_invoice_ocr_llm(image_path):

    result = ocr.ocr(image_path)

    text_lines = []

    if result and result[0]:
        for line in result[0]:
            text_lines.append(line[1][0])

    raw_text = "\n".join(text_lines)

    # Simulated LLM extraction
    # Replace with OpenAI/Gemma API

    extracted_data = {
        "invoice_number": "",
        "invoice_date": "",
        "vendor_name": "",
        "total_amount": "",
        "raw_text": raw_text
    }

    return extracted_data
