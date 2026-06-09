import json


class AdditiveDetector:

    def __init__(self, json_path):

        with open(json_path, "r") as f:
            self.additives = json.load(f)

    def detect(self, ingredients_text):

        ingredients_text = str(ingredients_text).lower()

        found = []

        for code, info in self.additives.items():

            if code.lower() in ingredients_text:
                found.append(
                    {
                        "code": code,
                        "name": info["name"],
                        "risk": info["risk"]
                    }
                )

        return found