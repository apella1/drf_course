"""Emulating endpoint consumption"""
import requests

PRODUCT_ID = input("Which ID do you want to use?\n")

try:
    PRODUCT_ID = int(PRODUCT_ID)
except ValueError:
    PRODUCT_ID = None
    print(f"{PRODUCT_ID} is not a valid integer ID")

if PRODUCT_ID is not None:
    ENDPOINT = f"http://127.0.0.1:8000/api/products/{PRODUCT_ID}/delete/"
    try:
        get_response = requests.delete(ENDPOINT, timeout=5)
        if get_response.status_code == 204:
            print(
                f"Product with ID {PRODUCT_ID} has been deleted successfully"
                )
        else:
            print(f"Failed to delete product with ID {PRODUCT_ID}.")
            print(f"Status code: {get_response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
else:
    print("No valid ID provided. Cannot proceed with your request")
