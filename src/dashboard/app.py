import sys
import os

# Ensure project root (fpna-forecasting-engine) is on sys.path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

import streamlit as st
import pandas as pd
from src.firestore.client import init_firestore
from src.forecasting.variance import calculate_variance

st.set_page_config(page_title="FP&A Forecasting Engine", layout="wide")

# Firestore client
db = init_firestore()

def load_collection(name: str) -> pd.DataFrame:
    docs = db.collection(name).stream()
    data = [d.to_dict() for d in docs]
    if not data:
        return pd.DataFrame()
    return pd.DataFrame(data)

st.title("📊 FP&A Forecasting Dashboard")

# --- Load data ---
actuals = load_collection("actuals")
budget = load_collection("budget")
forecast = load_collection("forecast")
scenarios = load_collection("scenarios")

# Guard against empty collections
if actuals.empty or budget.empty or forecast.empty:
    st.error("One or more collections are empty (actuals, budget, forecast). Run the pipelines first.")
    st.stop()

# --- Variance dataframe ---
variance_df = calculate_variance(actuals, budget, forecast)

# --- Executive KPIs ---
total_actuals = actuals["amount"].sum()
total_budget = budget["amount"].sum()
total_forecast = forecast["yhat"].sum()

variance_total = total_actuals - total_budget
variance_pct_total = (variance_total / total_budget) * 100 if total_budget != 0 else 0

st.header("Executive Summary")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Actuals", f"£{total_actuals:,.0f}")
k2.metric("Total Budget", f"£{total_budget:,.0f}")
k3.metric("Total Forecast", f"£{total_forecast:,.0f}")
k4.metric("Variance %", f"{variance_pct_total:.2f}%")

# --- Automated Insights ---
st.subheader("Automated Insights")

insights = []

if variance_total > 0:
    insights.append(f"📈 Actuals are **above budget** by £{variance_total:,.0f} ({variance_pct_total:.2f}%).")
elif variance_total < 0:
    insights.append(f"📉 Actuals are **below budget** by £{abs(variance_total):,.0f} ({variance_pct_total:.2f}%).")
else:
    insights.append("➖ Actuals are exactly on budget.")

if not scenarios.empty:
    base_sum = scenarios["base"].sum()
    best_sum = scenarios["best"].sum()
    worst_sum = scenarios["worst"].sum()

    if best_sum > base_sum:
        insights.append("✨ Best case scenario indicates potential upside versus base forecast.")
    if worst_sum < base_sum:
        insights.append("⚠️ Worst case scenario suggests possible downside risk versus base forecast.")
else:
    insights.append("ℹ️ Scenario data not found. Run the forecasting engine with scenarios enabled.")

for i in insights:
    st.write(i)

st.markdown("---")

# --- Records overview ---
col1, col2, col3 = st.columns(3)
col1.metric("Actuals Records", len(actuals))
col2.metric("Budget Records", len(budget))
col3.metric("Forecast Records", len(forecast))

# --- Actuals vs Budget vs Forecast ---
st.subheader("Actuals vs Budget vs Forecast")

actuals_ts = actuals.groupby("date")["amount"].sum()
budget_ts = budget.groupby("date")["amount"].sum()
forecast_ts = forecast.set_index("ds")["yhat"]

st.line_chart({
    "Actuals": actuals_ts,
    "Budget": budget_ts,
    "Forecast": forecast_ts
})

# --- Variance Analysis ---
st.subheader("Variance Analysis")

st.dataframe(variance_df)

st.line_chart({
    "Actuals": variance_df.set_index("date")["amount_actual"],
    "Budget": variance_df.set_index("date")["amount_budget"],
    "Forecast": variance_df.set_index("date")["forecast"],
    "Variance": variance_df.set_index("date")["variance"]
})

# --- Scenario Modelling ---
if not scenarios.empty:
    st.subheader("Scenario Modelling (Best / Base / Worst)")

    scenarios_ts = scenarios.set_index("ds")[["base", "best", "worst"]]

    st.line_chart({
        "Base Case": scenarios_ts["base"],
        "Best Case": scenarios_ts["best"],
        "Worst Case": scenarios_ts["worst"]
    })
else:
    st.info("Scenario collection is empty. Run the forecasting engine with scenario saving enabled.")
