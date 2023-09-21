"""Emulating endpoint consumption"""
import requests

ENDPOINT = "http://127.0.0.1:8000/api/products/59239847192347/"

get_response = requests.get(ENDPOINT, timeout=2000)

print(get_response.json())
