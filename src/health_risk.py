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

        # Sugar Risk

        
        if sugar <= 5:
            sugar_points = 0
        elif sugar <= 15:
            sugar_points = 10
        elif sugar <= 22.5:
            sugar_points = 20
        else:
            sugar_points = 25

        score += sugar_points

        # Salt Risk

        if salt <= 0.3:
            salt_points = 0
        elif salt <= 1.0:
            salt_points = 10
        elif salt <= 1.5:
            salt_points = 20
        else:
            salt_points = 25

        score += salt_points

        # Saturated Fat Risk

        if saturated_fat <= 1.5:
            fat_points = 0
        elif saturated_fat <= 3:
            fat_points = 10
        elif saturated_fat <= 5:
            fat_points = 20
        else:
            fat_points = 25

        score += fat_points

        # Energy Risk

        if energy <= 100:
            energy_points = 0
        elif energy <= 250:
            energy_points = 10
        elif energy <= 400:
            energy_points = 20
        else:
            energy_points = 25

        score += energy_points
        # Final Risk Level
        if score <= 20:
            level = "Low Risk"
        elif score <= 40:
            level = "Moderate Risk"
        elif score <= 70:
            level = "High Risk"
        else:
            level = "Very High Risk"

        return {
    "score": score,
    "risk_level": level,
    "factors": {
        "Sugar": sugar_points,
        "Salt": salt_points,
        "Saturated Fat": fat_points,
        "Energy": energy_points
    }
}