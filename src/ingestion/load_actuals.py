import pandas as pd
from google.cloud import firestore
from datetime import datetime
from src.firestore.client import init_firestore

def load_actuals(csv_path: str, collection_name: str = "actuals"):
    """
    Loads Actuals data from CSV and uploads to Firestore.
    Expected columns:
    - date
    - account
    - department
    - amount
    """

    # Read CSV
    df = pd.read_csv(csv_path)

    # Clean + standardise
    df.columns = [c.strip().lower() for c in df.columns]

    # Convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    # Connect to Firestore
    db = init_firestore()
    collection = db.collection(collection_name)

    # Upload row by row
    for _, row in df.iterrows():
        doc_id = f"{row['date'].strftime('%Y-%m-%d')}_{row['account']}"
        collection.document(doc_id).set(row.to_dict())

    print("Actuals uploaded successfully!")

if __name__ == "__main__":
    import sys

    # Default CSV path
    csv_path = "data/sample_actuals.csv"

    # If user passes a path, override it
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]

    load_actuals(csv_path)
