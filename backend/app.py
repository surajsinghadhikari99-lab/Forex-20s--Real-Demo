if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # backend/app.py
from flask import Flask, jsonify
import random, time

app = Flask(__name__)

# Demo forex pairs
pairs = ["EURUSD", "GBPUSD", "XAUUSD"]

@app.route("/predict/<pair>")
def predict(pair):
    pair = pair.upper()
    if pair not in pairs:
        return jsonify({"error": "Invalid pair"}), 400

    # Simple random prediction demo
    direction = random.choice(["UP", "DOWN", "FLAT"])
    confidence = round(random.uniform(55, 85), 2)

    return jsonify({
        "pair": pair,
        "prediction": direction,
        "confidence": f"{confidence}%",
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/")
def home():
    return "Forex AI Backend is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
