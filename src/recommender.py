class RecommendationEngine:

    def generate(
        self,
        allergens,
        risk
    ):

        recommendations = []

        # Allergens

        if "milk" in allergens:
            recommendations.append(
                "Avoid if lactose intolerant or allergic to milk."
            )

        if "peanuts" in allergens:
            recommendations.append(
                "Unsafe for peanut allergy sufferers."
            )

        if "soy" in allergens:
            recommendations.append(
                "Avoid if you have a soy allergy."
            )

        if "wheat" in allergens:
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