<div align="center">

# NutriInsightX

### AI-Powered Food Label Analysis & Nutrition Intelligence System

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=00C853&center=true&vCenter=true&width=900&lines=94.54%25+Random+Forest+Accuracy;190,969+Training+Samples;OCR+%2B+Machine+Learning+Pipeline;Nutri-Score+Prediction+A-E;Food+Label+Risk+Assessment" />

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Random_Forest-success?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Kaggle-190K%2B_Records-orange?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Accuracy-94.54%25-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## Overview

NutriInsightX is an AI-powered food label analysis platform that combines Optical Character Recognition (OCR), Machine Learning, and nutritional risk assessment to help users understand packaged food products.

The system extracts ingredient information from food labels, detects allergens and additives, evaluates health risks, and predicts Nutri-Score grades using a Random Forest classifier trained on the OpenFoodFacts Kaggle dataset.

---

## Key Achievements

<table>
<tr>
<td align="center" width="25%">

### 190,969

Training Samples

</td>

<td align="center" width="25%">

### 94.54%

Model Accuracy

</td>

<td align="center" width="25%">

### 7

Nutritional Features

</td>

<td align="center" width="25%">

### A-E

Nutri-Score Classes

</td>
</tr>
</table>

---

## Machine Learning Pipeline

```mermaid
flowchart TD

A["📦 OpenFoodFacts Dataset
190,969 Records"]

--> B["🧹 Data Cleaning"]

--> C["⚙️ Feature Selection"]

--> D["📊 Nutritional Features
Energy
Fat
Saturated Fat
Sugar
Protein
Fiber
Salt"]

--> E["✂️ Train-Test Split
80% / 20%"]

--> F["🌲 Random Forest Training"]

--> G["🔍 Hyperparameter Tuning"]

--> H["📈 Model Evaluation"]

--> I["🎯 Accuracy
94.54%"]

--> J["🏆 Nutri-Score Prediction
A • B • C • D • E"]
```
---

## Dataset

### Source

OpenFoodFacts (Kaggle)

### Records Used

190,969 Food Products

### Target Variable

```text
nutrition_grade_fr
```

### Features

```text
energy_100g
fat_100g
saturated-fat_100g
sugars_100g
proteins_100g
fiber_100g
salt_100g
```

---

## Model Performance

| Metric | Value |
|----------|----------|
| Dataset | OpenFoodFacts |
| Records | 190,969 |
| Algorithm | Random Forest |
| Accuracy | 94.54% |
| Target | nutrition_grade_fr |
| Classes | A, B, C, D, E |

### Classification Performance

| Grade | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| A | 0.97 | 0.95 | 0.96 |
| B | 0.90 | 0.91 | 0.91 |
| C | 0.93 | 0.94 | 0.94 |
| D | 0.96 | 0.96 | 0.96 |
| E | 0.97 | 0.94 | 0.96 |

---

## Features

<table>
<tr>
<td width="50%">

### OCR Food Label Analysis

- Image Upload
- Ingredient Extraction
- Food Label Processing
- Real Package Recognition

</td>

<td width="50%">

### Nutri-Score Prediction

- Random Forest Classifier
- Grade Prediction A-E
- Nutritional Feature Analysis
- ML-Based Classification

</td>
</tr>

<tr>
<td width="50%">

### Allergen Detection

- Milk
- Soy
- Wheat
- Gluten
- Peanuts
- Tree Nuts

</td>

<td width="50%">

### Health Risk Analysis

- Sugar Assessment
- Salt Assessment
- Saturated Fat Analysis
- Energy Evaluation

</td>
</tr>

<tr>
<td width="50%">

### Additive Detection

- Food Additives
- Preservatives
- Ingredient Screening
- Risk Awareness

</td>

<td width="50%">

### Personalized Recommendations

- Consumer Guidance
- Allergy Warnings
- Risk Insights
- Nutritional Suggestions

</td>
</tr>
</table>

---

## System Architecture

```text
Food Package Image
        │
        ▼
     EasyOCR
        │
        ▼
 Ingredient Extraction
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
Language Allergens Additives
Detect   Detect    Detect
        │
        ▼
 Health Risk Engine
        │
        ▼
 Random Forest Model
        │
        ▼
 Nutri-Score Prediction
        │
        ▼
 Recommendations
```

---

## Technology Stack

| Layer | Technologies |
|---------|---------|
| User Interface | Streamlit |
| Computer Vision | EasyOCR, OpenCV, Pillow |
| Machine Learning | Scikit-Learn, Random Forest |
| Data Processing | Pandas, NumPy |
| Language Detection | LangDetect |
| Visualization | Streamlit Charts, Matplotlib |
| Dataset | OpenFoodFacts (Kaggle) |
| Programming Language | Python 3.11 |

---

## Application Preview

### Light Theme

<p align="center">
  <img src="screenshots/light_home.png" width="900">
</p>

---

### Dark Theme

<p align="center">
  <img src="screenshots/dark_home.png" width="900">
</p>

---

### OCR Extraction

<p align="center">
  <img src="screenshots/ocr.png" width="900">
</p>

---

### Health Risk Analysis

<p align="center">
  <img src="screenshots/risk.png" width="900">
</p>

---

### Nutri-Score Prediction

<p align="center">
  <img src="screenshots/nutriscore.png" width="900">
</p>

---

## Project Structure

```text
NutriInsightX
│
├── app.py
├── preprocess.py
├── train_model.py
│
├── src
│   ├── ocr_engine.py
│   ├── allergen_detector.py
│   ├── additive_detector.py
│   ├── health_risk.py
│   ├── language_detector.py
│   ├── recommender.py
│   └── nutriscore_predictor.py
│
├── knowledge_base
│   ├── allergens.json
│   └── food_additives.json
│
├── screenshots
│
├── dataset
│
└── models
```

---

## Installation

```bash
git clone https://github.com/LovelySharma-dev/NutriInsightX.git

cd NutriInsightX

pip install -r requirements.txt

streamlit run app.py
```

---

## Future Enhancements

- SHAP Explainability Integration
- Barcode Scanner Support
- Real-Time Camera OCR
- Automated Nutrition Extraction
- Product Comparison Engine
- Mobile Application

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Final Year Report


**AI-Powered Food Label Analysis Using OCR and Machine Learning**