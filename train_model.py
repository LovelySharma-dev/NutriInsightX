import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df = pd.read_csv(
    "dataset/openfoodfacts_clean.csv",
    low_memory=False
)

features = [
    "energy_100g",
    "fat_100g",
    "saturated-fat_100g",
    "sugars_100g",
    "proteins_100g",
    "fiber_100g",
    "salt_100g"
]

target = "nutrition_grade_fr"

df = df[
    features + [target]
].dropna()

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test, predictions)
)

print(
    classification_report(
        y_test,
        predictions
    )
)

os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/nutriscore_model.pkl"
)

print("Model Saved")