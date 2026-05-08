import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore():
    cred = credentials.Certificate("credentials/serviceAccountKey.json")

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    return firestore.client()
