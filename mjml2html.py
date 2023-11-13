import requests

mjml_file_path = "./file.mjml"

with open(mjml_file_path, "r") as file:
    mjml_source = file.read()

# Define the MJML API endpoint
mjml_api_url = "https://api.mjml.io/v1/render"

# Replace 'YOUR_API_KEY' with your MJML API key
api_key = "api_key"

# Define the headers for the request, including the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the payload for the request
payload = {
    "mjml": mjml_source
}

# Send a POST request to the MJML API
response = requests.post(mjml_api_url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    if "html" in response_data:
        html_output = response_data["html"]
        print("Rendered HTML:")
        print(html_output)

        with open("output.html", "w") as output_file:
            output_file.write(html_output)

        print("HTML output written to output.html")
