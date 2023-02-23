import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {
    'title': ' This is a new title',
    'price': 20,
}

response = requests.put(endpoint, json=data)

print(response.json())