import requests
import json

login_url = "http://127.0.0.1:8000/api/login/"
login_data = {
    "username": "test_user",
    "password": "test_pass123",
    # "password2": "test_pass123",
    # "email": "test@test.com",
    # "phone": "1232456",
    # "first_name": "test",
    # "last_name": "test",
    # "country": "NG",
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
    "currency": 1,
}

response = requests.post(payment_url, json=data)
a = json.loads(response.text)
print(response.status_code)
print(a)


payment_url = "http://127.0.0.1:8001/api/confirm_payment/"
data = {"user_token": token, "token": "kz3vBjH3ohYk4Ny4geL8KiWFvqQPJYSg"}

response = requests.get(payment_url, json=data)
a = json.loads(response.text)
print(response.status_code)
print(a)


"""
payment_url = "http://127.0.0.1:8001/api/create_currency/"
data = {"user_token": "aa3c1b9badacb4738ccdf0037f676d1db139340f", "code": "USD", "name": "Доллар США"}

response = requests.post(payment_url, json=data)
a = json.loads(response.text)
print(response.status_code)
print(a)
"""
