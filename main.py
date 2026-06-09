import pandas as pd

from src.allergen_detector import AllergenDetector
from src.additive_detector import AdditiveDetector
from src.health_risk import HealthRiskScorer

allergen_detector = AllergenDetector(
    "knowledge_base/allergens.json"
)

additive_detector = AdditiveDetector(
    "knowledge_base/food_additives.json"
)

risk_scorer = HealthRiskScorer()

df = pd.read_csv(
    "dataset/openfoodfacts_clean.csv"
)

sample = df.iloc[0]

ingredients = str(sample["ingredients_text"])

print("Product:")
print(sample["product_name"])

print("\nIngredients:")
print(ingredients[:500])

print("\nAllergens:")
print(allergen_detector.detect(ingredients))

print("\nAdditives:")
print(additive_detector.detect(ingredients))

print("\nHealth Risk:")
print(
    risk_scorer.calculate(
        sample["sugars_100g"],
        sample["salt_100g"],
        sample["saturated-fat_100g"],
        sample["energy_100g"]
    )
)