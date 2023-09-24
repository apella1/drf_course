"""Emulating endpoint consumption"""
from getpass import getpass
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"

username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(
    AUTH_ENDPOINT, timeout=2000, json={"username": username, "password": password}
)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    ENDPOINT = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(ENDPOINT, timeout=2000, headers=headers)
    print(get_response.json())
