"""Emulating endpoint consumption"""
import requests

# endpoint = "https://httpbin.org/status/200"
# ENDPOINT = "https://httpbin.org/anything"
ENDPOINT = "http://127.0.0.1:8000/api/"

get_response = requests.get(
    ENDPOINT, params={"abc": 123}, json={"query": "Hello World"}, timeout=2000
)

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
