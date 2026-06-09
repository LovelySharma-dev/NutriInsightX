import streamlit as st
import tempfile
from src.ocr_engine import OCREngine
from src.allergen_detector import AllergenDetector
from src.additive_detector import AdditiveDetector
from src.health_risk import HealthRiskScorer
from src.utils import extract_ingredients
# Load modules
allergen_detector = AllergenDetector(
    "knowledge_base/allergens.json"
)

additive_detector = AdditiveDetector(
    "knowledge_base/food_additives.json"
)
risk_scorer = HealthRiskScorer()
ocr = OCREngine()

st.set_page_config(
    page_title="NutriInsightX",
    page_icon="🥗",
    layout="wide"
)

st.markdown("""
<style>
.stTextArea textarea {
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


st.title("🥗 NutriInsightX")
st.subheader("AI-Powered Food Label Analysis")
uploaded_file = st.file_uploader(
    "Upload Food Label Image",
    type=["jpg", "jpeg", "png"]
)

ocr_text = ""

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        tmp.write(uploaded_file.read())
        image_path = tmp.name

    raw_text = ocr.extract_text(image_path)

    ocr_text = extract_ingredients(
    raw_text
    )

    st.subheader("OCR Extracted Text")

    st.text_area(
        "OCR Result",
        ocr_text,
        height=150
    )

ingredients = st.text_area(
    "Enter Ingredients",
    value=ocr_text,
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
