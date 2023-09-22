"""Emulating endpoint consumption"""
import requests

ENDPOINT = "http://127.0.0.1:8000/api/products/10/update/"

data = {
    "title": "Hello from Python core team!",
    "content": "The core Python team is excited for you!",
    "price": 400.00,
}

get_response = requests.put(ENDPOINT, json=data, timeout=2000)

print(get_response.json())
