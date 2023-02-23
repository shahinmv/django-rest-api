import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.post(endpoint, params={'abc': 123}, json={'title': 'Hello world!', 'price': '155'})

print(response.json())