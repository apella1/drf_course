"""Emulating endpoint consumption"""
import requests

# endpoint = "https://httpbin.org/status/200"
# ENDPOINT = "https://httpbin.org/anything"
ENDPOINT = "http://127.0.0.1:8000/api/"

get_response = requests.post(
    ENDPOINT, json={"title": "This is a POST endpoint"}, timeout=2000
)

# print(get_response.text)
# print(get_response.headers)
# print(get_response.status_code)
print(get_response.json())
