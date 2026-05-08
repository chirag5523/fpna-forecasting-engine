import pandas as pd
from datetime import datetime
from src.firestore.client import init_firestore

def load_budget(csv_path: str, collection_name: str = "budget"):
    """
    Loads Budget data from CSV and uploads to Firestore.
    Expected columns:
    - date
    - account
    - department
    - amount
    """

    df = pd.read_csv(csv_path)
    df.columns = [c.strip().lower() for c in df.columns]

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    db = init_firestore()
    collection = db.collection(collection_name)

    for _, row in df.iterrows():
        doc_id = f"{row['date'].strftime('%Y-%m-%d')}_{row['account']}"
        collection.document(doc_id).set(row.to_dict())

    print("Budget uploaded successfully!")


if __name__ == "__main__":
    import sys

    csv_path = "data/sample_budget.csv"
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]

    load_budget(csv_path)
