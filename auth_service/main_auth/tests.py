import requests

url = 'http://127.0.0.1:8000/api/register/'
data = {
    'username': 'testuser3',
    'password': 'testpassword123',
    'password2': 'testpassword123',
    'token_api': '6b06d2f4d7c4e14e708e'
}

response = requests.post(url, json=data)
print(response.json())