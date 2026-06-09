from src.ocr_engine import OCREngine

ocr = OCREngine()

text = ocr.extract_text(
    "sample_food_label.jpg"
)

print(text)