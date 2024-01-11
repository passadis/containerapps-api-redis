from flask import Flask, request, jsonify
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from openai import OpenAI
import os
import redis
import json

app = Flask(__name__)

# Environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
storage_account_name = os.getenv('STORAGE_ACCOUNT_NAME')
container_name = 'cities'
#requirepass NWJRPMNAEKoXFVzAl1vwUjGYDSDR8E2w8sMxqN9ZSTYiX1VWwrIxqGQymaqkHB0PI9ZITH1MfIZXuU36VK0QxY7I2yaK29ozH0Wz2Kh8ZmblnnRWBnv1ULoygTw0liAOdir /mnt/dataport 6379protected-mode yesappendonly yes
redis_client = redis.Redis(host='citieskp.redis.cache.windows.net', port=6380, password='PwzPv9YPsJCNDAzhCQvYd05P04Go8LQqXAzCaAnMFsc=', ssl=True)
# Initialize OpenAI with the appropriate API key
client = OpenAI(
  organization='org-auCzDBnqqvQc40lcMtnwPzuK',
  api_key=OPENAI_API_KEY  # Use the environment variable here for security
)

# Initialize Azure credentials
credential = DefaultAzureCredential()

# Initialize Azure Blob Service Client with your account name and credential
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential)

@app.route('/get_city_info', methods=['POST'])
def get_city_info():
    city = request.form['city']

    # Check for cached response
    cached_response = redis_client.get(city)
    if cached_response:
        return jsonify(json.loads(cached_response))

    # Call OpenAI API to get the city description using the Chat model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Tell me about {city} with 100 words."}
        ]
    )
    print(response.choices[0].message)
    # Extracting the response text from the last message in the conversation
    description = response.choices[0].message.content

    # Get the city image from Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{city}.jpg')
    image_url = blob_client.url
    redis_client.setex(city, 86400, json.dumps({'description': description, 'image_url': image_url}))  # 86400 seconds = 24 hours
    # Return the description and image URL
    return jsonify({
        'description': description,
        'image_url': image_url
    })

if __name__ == '__main__':
    app.run(debug=True)
