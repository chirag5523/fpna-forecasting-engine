from client import init_firestore

db = init_firestore()

# Test write
db.collection("test").document("connection").set({"status": "ok"})

print("Firestore connection successful!")
