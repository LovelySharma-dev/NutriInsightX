class RecommendationEngine:

    def generate(
        self,
        allergens,
        risk
    ):

        recommendations = []

        allergen_names = [
            allergen["name"].lower()
            for allergen in allergens
        ]

        # Allergens

        if "milk" in allergen_names:
            recommendations.append(
                "Avoid if lactose intolerant or allergic to milk."
            )

        if "peanuts" in allergen_names:
            recommendations.append(
                "Unsafe for peanut allergy sufferers."
            )

        if "soy" in allergen_names:
            recommendations.append(
                "Avoid if you have a soy allergy."
            )

        if (
            "wheat" in allergen_names
            or
            "wheat & gluten" in allergen_names
        ):
            recommendations.append(
                "Not suitable for people with gluten sensitivity."
            )

        # Risk-based

        if risk["score"] >= 75:
            recommendations.append(
                "This product may be unhealthy if consumed frequently."
            )

        if risk["risk_level"] == "Very High Risk":
            recommendations.append(
                "Consider healthier alternatives with lower sugar, salt, and fat."
            )

        if not recommendations:
            recommendations.append(
                "No major concerns detected."
            )

        return recommendations