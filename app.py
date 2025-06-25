import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = joblib.load('final_model.pkl')

@app.route('/', methods=['GET', 'HEAD'])
def home():
    return render_template('home.html')

@app.route('/predict_page')
def predict_page():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the form
    input_data = request.form['features']
    features = [float(x) for x in input_data.split(',')]

    # Convert to a dataframe
    feature_names = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
                     'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
    data = pd.DataFrame([features], columns=feature_names)

    # Standardize the 'Amount' feature (you might need to standardize others depending on your model)
    sc = StandardScaler()
    data['Amount'] = sc.fit_transform(data[['Amount']])

    # Make a prediction
    prediction = model.predict(data)

    # Send the result back to the client
    output = 'Fraudulent' if prediction[0] == 1 else 'Not Fraudulent'

    return render_template('result.html', prediction_text=f'The transaction is likely: {output}')

if __name__ == '__main__':
    app.run(debug=True)
