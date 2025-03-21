import requests

url = 'http://127.0.0.1:8000/api/login/'
data = {
    'username': 'test_user3',
    'password': 'test_pass123',
}

response = requests.post(url, json=data)
print(response.json())