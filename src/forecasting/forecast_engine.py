import pandas as pd
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from src.firestore.client import init_firestore


def save_forecast_to_firestore(df, collection_name="forecast"):
    db = init_firestore()
    collection = db.collection(collection_name)

    for _, row in df.iterrows():
        doc_id = row["ds"].strftime("%Y-%m-%d")
        collection.document(doc_id).set(row.to_dict())

    print("Forecast saved to Firestore!")


def fetch_collection(collection_name):
    db = init_firestore()
    docs = db.collection(collection_name).stream()
    data = [doc.to_dict() for doc in docs]
    return pd.DataFrame(data)

def prepare_timeseries(df):
    df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
    df = df.groupby("date")["amount"].sum().reset_index()
    df = df.rename(columns={"date": "ds", "amount": "y"})
    return df

def prophet_forecast(df, periods=30):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]]

def arima_forecast(df, periods=30):
    model = ARIMA(df["y"], order=(2,1,2))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=periods)
    future_dates = pd.date_range(start=df["ds"].max() + pd.Timedelta(days=1), periods=periods)
    return pd.DataFrame({"ds": future_dates, "yhat_arima": forecast})

def run_forecast():
    actuals = fetch_collection("actuals")
    budget = fetch_collection("budget")

    actuals_ts = prepare_timeseries(actuals)
    budget_ts = prepare_timeseries(budget)

    prophet_out = prophet_forecast(actuals_ts)
    arima_out = arima_forecast(actuals_ts)

    combined = prophet_out.merge(arima_out, on="ds", how="left")

    print("Forecasting complete!")
    return combined

def generate_scenarios(forecast_df, uplift_pct=10, down_pct=10):
    df = forecast_df.copy()

    df["base"] = df["yhat"]
    df["best"] = df["yhat"] * (1 + uplift_pct / 100)
    df["worst"] = df["yhat"] * (1 - down_pct / 100)

    return df[["ds", "base", "best", "worst"]]



df = run_forecast()
scenarios = generate_scenarios(df)

print(scenarios.head())

save_forecast_to_firestore(scenarios, collection_name="scenarios")

