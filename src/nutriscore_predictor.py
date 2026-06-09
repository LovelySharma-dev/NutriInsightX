import joblib
import pandas as pd


class NutriScorePredictor:

    def __init__(self):

        self.model = joblib.load(
            "models/nutriscore_model.pkl"
        )

    def predict(
        self,
        energy,
        fat,
        saturated_fat,
        sugar,
        protein,
        fiber,
        salt
    ):

        data = pd.DataFrame([{
            "energy_100g": energy,
            "fat_100g": fat,
            "saturated-fat_100g": saturated_fat,
            "sugars_100g": sugar,
            "proteins_100g": protein,
            "fiber_100g": fiber,
            "salt_100g": salt
        }])

        prediction = self.model.predict(data)

        return prediction[0]