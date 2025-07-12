from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')
    product = data.get('product', 'Unknown Product')
    rating = data.get('rating', 'No Rating')

    if review.strip():
        X = vectorizer.transform([review])
        result = model.predict(X)[0]
        prediction = "Genuine" if result == 0 else "Fake"
    else:
        prediction = "Invalid input"

    return jsonify({
        'result': prediction,
        'product': product,
        'rating': rating
    })

if __name__ == '__main__':
    app.run(debug=True)
