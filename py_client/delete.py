"""Emulating endpoint consumption"""
import requests

product_id = input("Which id do you want to use?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid")

if product_id:
    ENDPOINT = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(ENDPOINT, timeout=2000)
    print(get_response.status_code, get_response.status_code == 204)
