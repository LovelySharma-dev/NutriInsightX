# src/ocr_engine.py

import easyocr

class OCREngine:

    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path):

        results = self.reader.readtext(image_path)

        text = []

        for item in results:
            text.append(item[1])

        return " ".join(text)