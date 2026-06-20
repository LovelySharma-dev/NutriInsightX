import json


class AllergenDetector:

    def __init__(self, json_path):

        with open(json_path, "r", encoding="utf-8") as f:
            self.allergens = json.load(f)

    def detect(self, ingredients_text):

        ingredients_text = str(
            ingredients_text
        ).lower()

        found = []

        for allergen, data in self.allergens.items():

            for keyword in data["keywords"]:

                if keyword.lower() in ingredients_text:

                    found.append({
                        "name": data["name"],
                        "category": data["category"],
                        "risk": data["risk"]
                    })

                    break

        return found