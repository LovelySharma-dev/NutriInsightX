<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,50:00693E,100:00C853&height=230&section=header&text=NutriInsightX&fontSize=64&fontColor=ffffff)

<!-- 🥗 NutriInsightX -->


### AI-Powered Food Label Analysis & Nutrition Intelligence System

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=00C853&center=true&vCenter=true&width=900&lines=94.54%25+Random+Forest+Accuracy;190%2C969+Training+Samples;OCR+%2B+Machine+Learning+Pipeline;Nutri-Score+Prediction+A-E;Food+Label+Risk+Assessment;Allergen+%26+Additive+Detection" />

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Random_Forest-success?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Dataset](https://img.shields.io/badge/Kaggle-190K%2B_Records-orange?style=for-the-badge&logo=kaggle&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-94.54%25-brightgreen?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

<br>

![Repo Size](https://img.shields.io/github/repo-size/LovelySharma-dev/NutriInsightX?style=flat-square&color=blueviolet)
![Last Commit](https://img.shields.io/github/last-commit/LovelySharma-dev/NutriInsightX?style=flat-square&color=blue)
![Issues](https://img.shields.io/github/issues/LovelySharma-dev/NutriInsightX?style=flat-square&color=red)
![Stars](https://img.shields.io/github/stars/LovelySharma-dev/NutriInsightX?style=social)
![Forks](https://img.shields.io/github/forks/LovelySharma-dev/NutriInsightX?style=social)

<br>

<a href="#-installation">
  <img src="https://img.shields.io/badge/🚀_Get_Started-black?style=for-the-badge" />
</a>
<a href="#-application-preview">
  <img src="https://img.shields.io/badge/📸_Screenshots-black?style=for-the-badge" />
</a>
<a href="#-model-performance">
  <img src="https://img.shields.io/badge/📊_Performance-black?style=for-the-badge" />
</a>
<a href="#-future-enhancements">
  <img src="https://img.shields.io/badge/🔮_Roadmap-black?style=for-the-badge" />
</a>

</div>

<br>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="100%">
</div>

---

## 📖 Table of Contents

<details open>
<summary>Click to expand</summary>

- [Overview](#-overview)
- [Key Achievements](#-key-achievements)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Application Preview](#-application-preview)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

</details>

---

## 🎯 Overview

**NutriInsightX** is an AI-powered food label analysis platform that combines **Optical Character Recognition (OCR)**, **Machine Learning**, and **nutritional risk assessment** to help users understand packaged food products at a glance.

The system extracts ingredient information from food labels, detects allergens and additives, evaluates health risks, and predicts Nutri-Score grades using a Random Forest classifier trained on the OpenFoodFacts Kaggle dataset — all wrapped in a clean, animated, dual-theme (light/dark) Streamlit interface.

> 💡 **Snap a label → Get instant nutrition intelligence.**

---

## 🏆 Key Achievements

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### 🗂️ 190,969
**Training Samples**

</td>

<td align="center" width="25%">

### 🎯 94.54%
**Model Accuracy**

</td>

<td align="center" width="25%">

### 📊 7
**Nutritional Features**

</td>

<td align="center" width="25%">

### 🔠 A–E
**Nutri-Score Classes**

</td>
</tr>
</table>

</div>

<div align="center">


![Random Forest](https://img.shields.io/badge/Random%20Forest-94.54%25-00C853?style=for-the-badge)
---

## ⚙️ Machine Learning Pipeline

```mermaid
flowchart TD

A["📦 OpenFoodFacts Dataset
190,969 Records"]

--> B["🧹 Data Cleaning"]

--> C["⚙️ Feature Selection"]

--> D["📊 Nutritional Features
Energy • Fat • Saturated Fat
Sugar • Protein • Fiber • Salt"]

--> E["✂️ Train-Test Split
80% / 20%"]

--> F["🌲 Random Forest Training"]

--> G["🔍 Hyperparameter Tuning"]

--> H["📈 Model Evaluation"]

--> I["🎯 Accuracy
94.54%"]

--> J["🏆 Nutri-Score Prediction
A • B • C • D • E"]

style A fill:#1a1a2e,stroke:#00C853,color:#fff
style J fill:#00C853,stroke:#00C853,color:#000
```

---

## 📂 Dataset

<table>
<tr>
<td width="50%">

**Source:** OpenFoodFacts (Kaggle)
**Records Used:** 190,969 Food Products
**Target Variable:**
```text
nutrition_grade_fr
```

</td>
<td width="50%">

**Features:**
```text
energy_100g
fat_100g
saturated-fat_100g
sugars_100g
proteins_100g
fiber_100g
salt_100g
```

</td>
</tr>
</table>

---

## 📊 Model Performance

<div align="center">

| Metric | Value |
|:--|:--|
| Dataset | OpenFoodFacts |
| Records | 190,969 |
| Algorithm | Random Forest |
| **Accuracy** | **94.54%** |
| Target | `nutrition_grade_fr` |
| Classes | A, B, C, D, E |

### Classification Performance

| Grade | Precision | Recall | F1-Score |
|:--:|:--:|:--:|:--:|
| 🟢 A | 0.97 | 0.95 | 0.96 |
| 🟢 B | 0.90 | 0.91 | 0.91 |
| 🟡 C | 0.93 | 0.94 | 0.94 |
| 🟠 D | 0.96 | 0.96 | 0.96 |
| 🔴 E | 0.97 | 0.94 | 0.96 |

</div>


<summary>📉 View accuracy trend across tuning iterations </summary>

```mermaid
xychart-beta
    title "Model Accuracy Across Tuning Iterations"
    x-axis ["Baseline", "Feature Selection", "Grid Search", "Final Tuned"]
    y-axis " Accuracy (%)" 80 --> 100
    bar [86.2, 89.7, 92.8, 94.54]

```



---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🔍 OCR Food Label Analysis
- Image Upload
- Ingredient Extraction
- Food Label Processing
- Real Package Recognition

</td>

<td width="50%" valign="top">

### 🏅 Nutri-Score Prediction
- Random Forest Classifier
- Grade Prediction A–E
- Nutritional Feature Analysis
- ML-Based Classification

</td>
</tr>

<tr>
<td width="50%" valign="top">

### ⚠️ Allergen Detection
- Milk
- Soy
- Wheat / Gluten
- Peanuts
- Tree Nuts

</td>

<td width="50%" valign="top">

### ❤️ Health Risk Analysis
- Sugar Assessment
- Salt Assessment
- Saturated Fat Analysis
- Energy Evaluation

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🧪 Additive Detection
- Food Additives
- Preservatives
- Ingredient Screening
- Risk Awareness

</td>

<td width="50%" valign="top">

### 🎁 Personalized Recommendations
- Consumer Guidance
- Allergy Warnings
- Risk Insights
- Nutritional Suggestions

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A["📷 Food Package Image"] --> B["🔎 EasyOCR"]
    B --> C["📝 Ingredient Extraction"]
    C --> D["🌐 Language Detection"]
    C --> E["⚠️ Allergen Detection"]
    C --> F["🧪 Additive Detection"]
    D --> G["❤️ Health Risk Engine"]
    E --> G
    F --> G
    G --> H["🌲 Random Forest Model"]
    H --> I["🏅 Nutri-Score Prediction"]
    I --> J["🎁 Recommendations"]

    style A fill:#1a1a2e,stroke:#00C853,color:#fff
    style J fill:#00C853,stroke:#00C853,color:#000
```

---

## 🛠️ Technology Stack

<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

| Layer | Technologies |
|:--|:--|
| User Interface | Streamlit |
| Computer Vision | EasyOCR, OpenCV, Pillow |
| Machine Learning | Scikit-Learn, Random Forest |
| Data Processing | Pandas, NumPy |
| Language Detection | LangDetect |
| Visualization | Streamlit Charts, Matplotlib |
| Dataset | OpenFoodFacts (Kaggle) |
| Programming Language | Python 3.11 |

---

## 📸 Application Preview

<div align="center">

**Toggle between themes to see NutriInsightX adapt in real time ☀️ / 🌙**

</div>

### ☀️ Light Theme

<table>
<tr>
<td align="center" width="33%">
<img src="screenshots/light_dashboard_1.png" width="100%"><br>
<sub><b>Dashboard — Home Overview</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/light_dashboard_2.png" width="100%"><br>
<sub><b>Dashboard — Upload Panel</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/light_run_1.png" width="100%"><br>
<sub><b>Run — OCR Processing</b></sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
<img src="screenshots/light_run_2.png" width="100%"><br>
<sub><b>Run — Live Analysis</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/light_output_1.png" width="100%"><br>
<sub><b>Output — Nutri-Score Result</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/light_output_2.png" width="100%"><br>
<sub><b>Output — Risk & Allergen Report</b></sub>
</td>
</tr>
</table>

---

### 🌙 Dark Theme

<table>
<tr>
<td align="center" width="33%">
<img src="screenshots/dark_dashboard_1.png" width="100%"><br>
<sub><b>Dashboard — Home Overview</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/dark_dashboard_2.png" width="100%"><br>
<sub><b>Dashboard — Upload Panel</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/dark_run_1.png" width="100%"><br>
<sub><b>Run — OCR Processing</b></sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
<img src="screenshots/dark_run_2.png" width="100%"><br>
<sub><b>Run — Live Analysis</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/dark_output_1.png" width="100%"><br>
<sub><b>Output — Nutri-Score Result</b></sub>
</td>
<td align="center" width="33%">
<img src="screenshots/dark_output_2.png" width="100%"><br>
<sub><b>Output — Risk & Allergen Report</b></sub>
</td>
</tr>
</table>

<details>
<summary>🗂️ Full screenshot file checklist (12 total — click to expand)</summary>

**Light Mode (6)**
- `screenshots/light_dashboard_1.png` — Home overview
- `screenshots/light_dashboard_2.png` — Upload panel
- `screenshots/light_run_1.png` — OCR processing in progress
- `screenshots/light_run_2.png` — Live analysis / spinner state
- `screenshots/light_output_1.png` — Nutri-Score result card
- `screenshots/light_output_2.png` — Risk & allergen report

**Dark Mode (6)**
- `screenshots/dark_dashboard_1.png` — Home overview
- `screenshots/dark_dashboard_2.png` — Upload panel
- `screenshots/dark_run_1.png` — OCR processing in progress
- `screenshots/dark_run_2.png` — Live analysis / spinner state
- `screenshots/dark_output_1.png` — Nutri-Score result card
- `screenshots/dark_output_2.png` — Risk & allergen report

> Drop your captured images into the `screenshots/` folder using these exact filenames and they'll render automatically above.

</details>

---

## 📁 Project Structure

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
│   ├── light_dashboard_1.png
│   ├── light_dashboard_2.png
│   ├── light_run_1.png
│   ├── light_run_2.png
│   ├── light_output_1.png
│   ├── light_output_2.png
│   ├── dark_dashboard_1.png
│   ├── dark_dashboard_2.png
│   ├── dark_run_1.png
│   ├── dark_run_2.png
│   ├── dark_output_1.png
│   └── dark_output_2.png
│
├── dataset
│
└── models
```

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/LovelySharma-dev/NutriInsightX.git

# 2. Move into the project directory
cd NutriInsightX

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

<div align="center">

Then open your browser at **`http://localhost:8501`** 🎉

</div>

---

## 🔮 Future Enhancements

- [ ] SHAP Explainability Integration
- [ ] Barcode Scanner Support
- [ ] Real-Time Camera OCR
- [ ] Automated Nutrition Extraction
- [ ] Product Comparison Engine
- [ ] Mobile Application

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 🎓 Final Year Report

**AI-Powered Food Label Analysis Using OCR and Machine Learning**

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

</div>