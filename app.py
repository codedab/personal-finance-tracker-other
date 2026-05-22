from flask import Flask, jsonify
from collections import defaultdict
from finance_tracker import load_transactions, summarise
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Personal Finance Tracker API is live",
        "endpoints": ["/summary", "/health"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/summary")
def summary():
    path = os.path.join("data", "transactions.csv")
    transactions = load_transactions(path)
    result = []
    for tx in transactions:
        result.append({
            "month": tx["month"],
            "description": tx["description"],
            "amount": tx["amount"],
            "type": tx["type"],
            "category": tx["category"]
        })
    return jsonify({"total": len(result), "transactions": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)