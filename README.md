# fpna-forecasting-engine
End-to-end FP&amp;A revenue and expense forecasting engine using Python, Firestore, and Streamlit.

# FP&A Forecasting Engine

End-to-end FP&A engine with:
- Actuals + Budget ingestion
- Prophet + ARIMA forecasting
- Scenario modelling (Best / Base / Worst)
- Variance analysis
- Streamlit executive dashboard

## 1. Features

- 🔄 Firestore-backed data store
- 📈 Time-series forecasting (Prophet + ARIMA)
- 🎯 Scenario modelling (best/base/worst)
- 📊 Executive dashboard (KPIs, variance, insights)

## 2. Tech stack

- Python 3.11+
- pandas, prophet, statsmodels
- Google Firestore
- Streamlit

## 3. Setup

```bash
git clone <repo-url>
cd fpna-forecasting-engine
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
