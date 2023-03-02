import requests
import json

# Load Grocy API URL, product IDs, and API key from the JSON file
with open('settings.json') as f:
    grocy_config = json.load(f)

grocy_url = grocy_config['grocy_url']
product_ids = grocy_config['product_ids']
api_key = grocy_config['api_key']

# Set up headers for authentication
headers = {'GROCY-API-KEY': api_key, 'Content-Type': 'application/json'}

# Loop through each product ID and consume 1 unit per day
for product_id in product_ids:
    consume_data = {"amount": 1, "transaction_type": "consume", "spoiled": False}
    response = requests.post(f"{grocy_url}/api/stock/products/{product_id}/consume", headers=headers, json=consume_data)
    print(f"Consumed 1 unit of product with ID {product_id}. Status code: {response.status_code}")
