import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': 'This field is done',
    'price': 35.99
}

response = requests.post(endpoint, json=data)

print(response.json())