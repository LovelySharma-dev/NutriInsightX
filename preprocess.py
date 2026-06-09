import pandas as pd

# Columns needed for NutriInsightX
cols = [
    "code",
    "product_name",
    "brands",
    "categories_en",
    "ingredients_text",
    "allergens",
    "allergens_en",
    "traces",
    "additives_n",
    "additives_tags",
    "additives_en",
    "energy_100g",
    "fat_100g",
    "saturated-fat_100g",
    "sugars_100g",
    "proteins_100g",
    "fiber_100g",
    "salt_100g",
    "nutrition_grade_fr"
]

print("Loading dataset...")

df = pd.read_csv(
    "dataset/openfoodfacts_clean.csv",
    sep="\t",
    low_memory=False
)

# Keep only required columns
clean_df = df[cols]

print("\nMissing Values:")
print(clean_df.isnull().sum())

# Remove products with no ingredient list
clean_df = clean_df.dropna(
    subset=["ingredients_text"]
)

print("\nFinal Shape:")
print(clean_df.shape)

# Save cleaned dataset
clean_df.to_csv(
    "dataset/openfoodfacts_clean.csv",
    index=False
)

print("\nSaved: dataset/openfoodfacts_clean.csv")