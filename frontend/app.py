from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

storage_account_name = os.getenv('STORAGE_ACCOUNT_NAME')
backend_api_url = os.getenv('BACKEND_API_URL')

@app.route('/')
def index():
    # Just render the initial form
    return render_template('index.html')

@app.route('/get_city_info', methods=['POST'])
def get_city_info():
    city = request.form.get('city')

    # Call the backend service using form data
    response = requests.post(f"{backend_api_url}/get_city_info", data={"city": city})
    if response.status_code == 200:
        data = response.json()
        description = data.get('description', "No description available")
        image_url = data.get('image_url', f"https://{storage_account_name}.blob.core.windows.net/cities/{city}.jpg")
    else:
        # Fallback in case of an error
        description = "Error fetching data"
        image_url = f"https://{storage_account_name}.blob.core.windows.net/cities/{city}.jpg"

    # The AJAX call expects a JSON response
    return jsonify(description=description, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=False)
