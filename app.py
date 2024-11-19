from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the models
rf_model = joblib.load('random_forest_model.pkl')
nn_model = joblib.load('neural_network_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Phishing URL Detection API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from the request
    
    # Assuming data contains a list of features to predict
    features = np.array([data['features']])
    
    # Predict using Random Forest model
    rf_prediction = rf_model.predict(features)
    # Predict using Neural Network model
    nn_prediction = nn_model.predict(features)
    
    response = {
        'rf_prediction': int(rf_prediction[0]),
        'nn_prediction': int(nn_prediction[0])
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
