from flask import Flask, jsonify

app = Flask(gunicorn app:app)

@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({
        'pair1': 'EURUSD',
        'pair2': 'GBPUSD',
        'pair3': 'USDJPY',
        'signal1': 'UP',
        'signal2': 'DOWN',
        'signal3': 'UP'
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
