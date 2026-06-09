import json


class AllergenDetector:

    def __init__(self, json_path):

        with open(json_path, "r") as f:
            self.allergens = json.load(f)

    def detect(self, ingredients_text):

        ingredients_text = str(ingredients_text).lower()

        found = []

        for allergen, keywords in self.allergens.items():

            for keyword in keywords:

                if keyword.lower() in ingredients_text:
                    found.append(allergen)
                    break

        return found
    
    