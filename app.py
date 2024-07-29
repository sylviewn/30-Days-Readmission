from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model at the start
model = joblib.load('linear_reg_simplified.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form
        data = request.form['YTD_Rate']
        ytd_rate = float(data)

        # Debug: Print the input data
        print(f"Input YTD Rate: {ytd_rate}")

        # Make a prediction
        prediction = model.predict(np.array([[ytd_rate]]))

        # Debug: Print the prediction
        print(f"Prediction: {prediction[0]}")

        # Return the prediction in the HTML template
        return render_template('index.html', prediction_text=f'Predicted Readmission Rate: {prediction[0]:.4f}')
    except Exception as e:
        # Handle any errors and return an error message in JSON format
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





