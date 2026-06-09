import streamlit as st
import tempfile

from src.ocr_engine import OCREngine
from src.allergen_detector import AllergenDetector
from src.additive_detector import AdditiveDetector
from src.health_risk import HealthRiskScorer
from src.utils import extract_ingredients
from src.language_detector import LanguageDetector
from src.recommender import RecommendationEngine


# Load modules
@st.cache_resource
def load_ocr():
    return OCREngine()

ocr = load_ocr()
allergen_detector = AllergenDetector(
    "knowledge_base/allergens.json"
)

additive_detector = AdditiveDetector(
    "knowledge_base/food_additives.json"
)
risk_scorer = HealthRiskScorer()
language_detector = LanguageDetector()
recommender = RecommendationEngine()

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
    # print("OCR RUNNING")
    ocr_text = extract_ingredients(
    raw_text
    )

    st.subheader("OCR Extracted Text")

    st.text_area(
        "Processed Label Text",
        ocr_text,
        height=200
    )

ingredients = st.text_area(
    "Enter Ingredients",
    value=ocr_text,
    height=200,
    placeholder="Paste ingredients here..."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    sugar = st.number_input(
    "Sugar (g / 100g)",
    min_value=0.0,
    max_value=100.0,
    value=0.0
)

with col2:
    salt = st.number_input("Salt (g)", min_value=0.0)

with col3:
    saturated_fat = st.number_input(
    "Saturated Fat (g / 100g)",
    min_value=0.0,
    max_value=100.0,
    value=0.0
)

with col4:
    energy = st.number_input(
    "Energy (kcal / 100g)",
    min_value=0.0,
    max_value=1000.0,
    value=0.0
)
if st.button("Analyze Food"):
    language = language_detector.detect_language(
        ingredients
    )
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
    recommendations = recommender.generate(
    allergens,
    risk
    )
    st.divider()
    st.subheader("Detected Language")

    st.info(language.upper())
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
    st.subheader("Personalized Recommendations")

    for rec in recommendations:
       st.info(rec)
    st.metric(
        "Risk Score",
        risk["score"]
    )
    st.subheader("Risk Breakdown")

    for factor, points in risk["factors"].items():
       st.write(f"{factor}: +{points}")
    st.info(
        f"Risk Level: {risk['risk_level']}"
    )
