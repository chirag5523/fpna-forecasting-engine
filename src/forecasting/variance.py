import pandas as pd

def calculate_variance(actuals, budget, forecast):
    actuals = actuals.copy()
    budget = budget.copy()
    forecast = forecast.copy()

    actuals["date"] = pd.to_datetime(actuals["date"])
    budget["date"] = pd.to_datetime(budget["date"])
    forecast["ds"] = pd.to_datetime(forecast["ds"])

    actuals_daily = actuals.groupby("date")["amount"].sum().reset_index()
    budget_daily = budget.groupby("date")["amount"].sum().reset_index()
    forecast_daily = forecast.rename(columns={"ds": "date", "yhat": "forecast"})

    df = actuals_daily.merge(budget_daily, on="date", how="left", suffixes=("_actual", "_budget"))
    df = df.merge(forecast_daily[["date", "forecast"]], on="date", how="left")

    df["variance"] = df["amount_actual"] - df["amount_budget"]
    df["variance_pct"] = (df["variance"] / df["amount_budget"]) * 100

    return df
