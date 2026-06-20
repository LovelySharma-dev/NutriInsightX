import json


class AdditiveDetector:

    def __init__(self, json_path):

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.additives = json.load(f)

    def detect(self, ingredients_text):

        ingredients_text = str(
            ingredients_text
        ).lower()

        found = []

        for group, additives in self.additives.items():

            for code, data in additives.items():

                for keyword in data["keywords"]:

                    if keyword.lower() in ingredients_text:

                        found.append(
                            {
                                "code": code,
                                "name": data["name"],
                                "category": data["category"],
                                "risk": data["risk"]
                            }
                        )

                        break

        return found