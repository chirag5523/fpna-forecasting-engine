# FP&A Forecasting Engine  
End‑to‑end FP&A revenue & expense forecasting engine using **Python**, **Firestore**, and **Streamlit** — complete with forecasting, scenarios, variance analysis, and an executive dashboard.

---

## 📌 Badges

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![Firestore](https://img.shields.io/badge/Firestore-Enabled-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)

---

## 🚀 Overview

This project is a **production‑style FP&A forecasting engine** designed to automate:

- Actuals & Budget ingestion  
- Prophet + ARIMA forecasting  
- Scenario modelling (Best / Base / Worst)  
- Variance analysis  
- Executive dashboard with KPIs & insights  

It is built to mimic real FP&A workflows used in Finance teams, but with a clean, modular, Python‑based architecture.

---

## 🧱 Architecture

┌──────────────────────────────┐
│        Streamlit UI          │
│  Executive Dashboard (KPIs)  │
│  Variance & Scenario Charts  │
└───────────────┬──────────────┘
│
▼
┌──────────────────────────────┐
│     Forecasting Engine       │
│ Prophet + ARIMA Models       │
│ Scenario Generator           │
└───────────────┬──────────────┘
│
▼
┌──────────────────────────────┐
│         Firestore DB         │
│ actuals / budget / forecast  │
│ scenarios / adjustments      │
└──────────────────────────────┘

Code

---

## ✨ Features

### 🔄 Data Ingestion  
- Load Actuals & Budget from CSV or Firestore  
- Demo mode with sample data  

### 📈 Forecasting  
- Prophet for trend & seasonality  
- ARIMA for statistical validation  
- Forecast stored in Firestore  

### 🎯 Scenario Modelling  
- Base case  
- Best case (+10%)  
- Worst case (–10%)  

### 📊 Variance Analysis  
- Daily variance  
- Cumulative variance  
- Variance %  
- Actuals vs Budget vs Forecast  

### 🧠 Automated Insights  
- Variance commentary  
- Scenario risk/opportunity signals  
- Executive‑ready summary  

---

## 📂 Project Structure

fpna-forecasting-engine/
│
├── src/
│   ├── firestore/
│   │   └── client.py
│   ├── forecasting/
│   │   ├── forecast_engine.py
│   │   └── variance.py
│   ├── dashboard/
│   │   └── app.py
│   └── data/
│       └── load_sample_data.py
│
├── data/
│   ├── sample_actuals.csv
│   └── sample_budget.csv
│
├── credentials/
│   └── serviceAccountKey.json
│
├── requirements.txt
├── .env.example
└── README.md

Code

---

## ⚙️ Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/chirag5523/fpna-forecasting-engine.git
cd fpna-forecasting-engine
2️⃣ Create virtual environment
bash
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
bash
pip install -r requirements.txt
🔐 Firestore Setup
Place your Google service account key here:

Code
credentials/serviceAccountKey.json
Set environment variable:

PowerShell (Windows):

powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="D:\path\to\fpna-forecasting-engine\credentials\serviceAccountKey.json"
🧪 Demo Mode (Sample Data)
Load sample Actuals & Budget:

bash
python -m src.data.load_sample_data
🔮 Run Forecasting Engine
bash
python -m src.forecasting.forecast_engine
This generates:

Forecast

Best/Base/Worst scenarios

Saves everything to Firestore

📊 Launch Dashboard
bash
streamlit run src/dashboard/app.py
Dashboard includes:

Executive KPIs

Automated insights

Actuals vs Budget vs Forecast

Variance analysis

Scenario modelling

🖼️ Screenshots
Add your screenshots here:

Dashboard overview (assets/Dashboard overview.png)

Variance analysis (assets/Variance analysis.png)

Scenario modelling (assets/Scenario modelling.png)

![Architecture Diagram](assets/architecture.png)



---------------
⚙️ How to Run the FP&A Engine
1️⃣ Clone the repository
bash
git clone https://github.com/chirag5523/fpna-forecasting-engine.git
cd fpna-forecasting-engine
2️⃣ Create and activate a virtual environment
Windows (PowerShell):

powershell
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
pip install -r requirements.txt
4️⃣ Configure Firestore credentials
Place your Google service account key here:

Code
credentials/serviceAccountKey.json
Set the environment variable:

powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="D:\path\to\fpna-forecasting-engine\credentials\serviceAccountKey.json"
5️⃣ Load sample data (Demo Mode)
bash
python -m src.data.load_sample_data
6️⃣ Run the forecasting engine
bash
python -m src.forecasting.forecast_engine
This generates:

Forecast

Best/Base/Worst scenarios

Saves everything to Firestore

7️⃣ Launch the dashboard
bash
streamlit run src/dashboard/app.py
You now have:

Executive KPIs

Variance analysis

Scenario modelling

Automated insights

Actuals vs Budget vs Forecast