# 🌍 AI-Based Air Quality Prediction and Health Alert System

## 📌 Project Overview
This project is an AI-based software system that predicts the **current Air Quality Index (AQI)** for a selected city using historical air pollution data. The system provides easy-to-understand AQI categories and health advisories to help users take timely preventive actions. The solution is fully software-based and focuses on sustainability and public health awareness.

---

## ❓ Problem Statement
Urban air pollution poses serious health risks, but most people lack timely and easy-to-understand information about current air quality conditions. Existing systems often provide raw data that is difficult to interpret. There is a need for a simple AI-based solution that can predict the current AQI for a city and provide clear health advisories to reduce pollution-related health risks.

---

## 🎯 Objectives
- Predict the current AQI for urban cities using AI
- Simulate real-world usage using historical air quality data
- Provide clear AQI categories and health advisories
- Build a simple, explainable, and functional software prototype

---

## 🌱 SDG Alignment
- **Primary SDG:** SDG 3 – Good Health and Well-Being  
- **Secondary SDG:** SDG 11 – Sustainable Cities and Communities  

---

## 🧠 Solution Description (Including AI Elements)
The proposed solution automatically retrieves the most recent available air pollution data for a selected city from a dataset and uses a Linear Regression machine learning model to predict the current AQI. The model analyzes key pollutants such as PM2.5, PM10, NO₂, SO₂, and CO to estimate the AQI value. Based on the predicted AQI, the system categorizes air quality levels and provides corresponding health advisories. The use of AI enables data-driven prediction rather than simple rule-based reporting.

---

## 👥 Target Users
- Urban residents  
- Students and working professionals  
- Elderly people and individuals with respiratory conditions  
- Institutions and city authorities for awareness purposes  

---

## 🔄 System Workflow

1. User selects a **city**
2. System fetches the **most recent available air quality data** for that city
3. Relevant pollutant values are extracted
4. Data is passed to the **Linear Regression model**
5. Model predicts the **AQI value**
6. AQI category and **health advisory** are displayed

### Workflow Diagram
City Selection
↓
Fetch Latest City Data
↓
Pollutant Feature Extraction
↓
Linear Regression Model
↓
AQI Prediction
↓
AQI Category & Health Advisory

---

## 🛠️ Technologies Used
Python is used as the core programming language for the project. Machine learning is implemented using the Scikit-learn library, where a Linear Regression model is used for AQI prediction. Pandas is used for loading and processing the air quality dataset in CSV format. Streamlit is used to build a simple and interactive web-based user interface. The project uses a public air quality dataset and runs completely as a software-only solution.

---

## 📁 Project Structure
air_quality_proto/
│
├── data/
│ └── aqi_data.csv
│
├── model.py
├── app.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project
1. Install required libraries:
```bash
pip install streamlit pandas scikit-learn
streamlit run app.py
