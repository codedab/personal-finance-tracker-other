from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Finance Tracker is live"})

@app.route("/summary")
def summary():
    data = pd.read_csv("data/transactions.csv")
    food = 0
    transport = 0
    other = 0
    for i in range(len(data)):
        if data["description"][i] == "food":
            food += data["amount"][i]
        elif data["description"][i] == "transport":
            transport += data["amount"][i]
        else:
            other += data["amount"][i]
    return jsonify({"food": int(food), "transport": int(transport), "other": int(other)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)