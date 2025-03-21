import requests
import json

login_url = "http://127.0.0.1:8000/api/login/"
login_data = {
    "username": "test_user3",
    "password": "test_pass123",
}
login_response = requests.post(login_url, json=login_data)
token = login_response.json().get("token")
print(token)
print(login_response.json())

payment_url = "http://127.0.0.1:8001/api/create_payment/"
data = {
    "token": token,
    "product": "Premium Subscription",
    "amount": 50000,
    "currency": "NGN",
}

response = requests.post(payment_url, json=data)
a = json.loads(response.text)
print(response.status_code)
print(a)


payment_url = 'http://127.0.0.1:8001/api/confirm_payment/'
data = {
  "user_token": token,
  "token": response.json().get("token")
}

response = requests.get(payment_url, json=data)
a = json.loads(response.text)
print(response.status_code)  
print(a)

