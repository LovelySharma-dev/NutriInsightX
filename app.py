import streamlit as st

from src.allergen_detector import AllergenDetector
from src.additive_detector import AdditiveDetector
from src.health_risk import HealthRiskScorer

# Load modules
allergen_detector = AllergenDetector(
    "knowledge_base/allergens.json"
)

additive_detector = AdditiveDetector(
    "knowledge_base/food_additives.json"
)

risk_scorer = HealthRiskScorer()

st.set_page_config(
    page_title="NutriInsightX",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 NutriInsightX")
st.subheader("AI-Powered Food Label Analysis")

ingredients = st.text_area(
    "Enter Ingredients",
    height=200,
    placeholder="Paste ingredients here..."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    sugar = st.number_input("Sugar (g)", min_value=0.0)

with col2:
    salt = st.number_input("Salt (g)", min_value=0.0)

with col3:
    saturated_fat = st.number_input(
        "Saturated Fat (g)",
        min_value=0.0
    )

with col4:
    energy = st.number_input(
        "Energy (kcal)",
        min_value=0.0
    )

if st.button("Analyze Food"):

    allergens = allergen_detector.detect(
        ingredients
    )

    additives = additive_detector.detect(
        ingredients
    )

    risk = risk_scorer.calculate(
        sugar,
        salt,
        saturated_fat,
        energy
    )

    st.divider()

    st.subheader("Detected Allergens")

    if allergens:
        st.warning(", ".join(allergens))
    else:
        st.success("✅ No allergens detected")

    st.subheader("Detected Additives")

    if additives:
        for additive in additives:
            st.error(
                f"{additive['code']} - "
                f"{additive['name']}\n\n"
                f"Risk: {additive['risk']}"
            )
    else:
        st.success("✅ No additives detected")

    st.subheader("Health Risk Score")

    st.metric(
        "Risk Score",
        risk["score"]
    )

    st.info(
        f"Risk Level: {risk['risk_level']}"
    )
    