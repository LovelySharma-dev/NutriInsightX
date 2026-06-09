class HealthRiskScorer:

    def calculate(
        self,
        sugar,
        salt,
        saturated_fat,
        energy
    ):

        score = 0

        try:
            sugar = float(sugar)
        except:
            sugar = 0

        try:
            salt = float(salt)
        except:
            salt = 0

        try:
            saturated_fat = float(saturated_fat)
        except:
            saturated_fat = 0

        try:
            energy = float(energy)
        except:
            energy = 0

        if sugar > 22.5:
            score += 25

        if salt > 1.5:
            score += 25

        if saturated_fat > 5:
            score += 25

        if energy > 400:
            score += 25

        if score <= 25:
            level = "Low Risk"
        elif score <= 50:
            level = "Moderate Risk"
        elif score <= 75:
            level = "High Risk"
        else:
            level = "Very High Risk"

        return {
            "score": score,
            "risk_level": level
        }