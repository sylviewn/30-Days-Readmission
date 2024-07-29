import requests
import json

# Define the URL of the API
url = "https://mentalhealth-webapp.azurewebsites.net/predict"
headers = {"Content-Type": "application/json"}

# Define a list of test cases with different YTD_Rate values
test_cases = [
    {"YTD_Rate": 0.10},
    {"YTD_Rate": 0.15},
    {"YTD_Rate": 0.20},
    {"YTD_Rate": 0.25},
    {"YTD_Rate": 0.30},
    {"YTD_Rate": 0.35},
    {"YTD_Rate": 0.40}
]

# Function to send a POST request and print the response
def test_api(data):
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"Request data: {data}, Response: {response.json()}")

# Iterate over each test case and call the test_api function
for case in test_cases:
    test_api(case)


