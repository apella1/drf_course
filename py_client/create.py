"""Emulating endpoint consumption"""
import requests

ENDPOINT = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "Hiking Boots",
    # "content": "These are the best hiking boots!",
    "price": 890,
}

get_response = requests.post(ENDPOINT, timeout=2000, data=data)

print(get_response.json())
