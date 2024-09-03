import requests
import json

# Define your API endpoint
container_url = "http://localhost:5002/predict"

# Load your JSON data (already mounted into the container)
with open('sample_input_data.json', 'r') as json_file:
    input_data = json.load(json_file)

# Send a POST request to the container
response = requests.post(container_url, json=input_data)

# Extract the output from the response
output_data = response.json()

print("Output from container:", output_data)
