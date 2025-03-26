# Payment-System

API для взаимодействия с платежной системой https://docs.processinprocess.com

## Установка

1. Клонируйте репозиторий:

`git clone https://github.com/Leila132/Payment-System.git`

2. Перейдите в директорию проекта:

`cd Payment-System`

3. Установите зависимости:

`pip install -r requirements.txt`

4. Создайте файл с переменными окружения:

.env
-`PG_PASSWORD = ""`
-`PG_USER = ""`
-`PG_DB_NAME = ""`
-`PG_PORT = ""`
-`AUTH_SECRET_KEY = ""`
-`PAYMENT_SECRET_KEY = ""`
-`SANDBOX_URL = ''`
-`API_TOKEN = ""`
-`PAYMENTS_URL = ""`
-`CONFIRM_URL = ""`
-`DECLINE_URL = ""`
-`AUTH_API_URL = "http://***/api/verify-token/"`

5. Проведите миграции:

`python manage.py migrate`

## Использование

1. POST /api/register/
data = {
    "username": "test_user",
    "password": "test_pass123",
    "password2": "test_pass123",
    "email": "test@test.com",
    "phone": "1232456",
    "first_name": "test",
    "last_name": "test",
    "country": "NG"
}

2. POST /api/login/
data = {
    "username": "test_user",
    "password": "test_pass123"
}

3. POST /api/verify-token/
data = {
    "token": "token_key"
}

4. POST /api/create_currency/
data = {
    "user_token": "user_token", 
    "code": "USD", 
    "name": "Доллар США"
}

5. POST /api/create_payment/
data = {
    "token": "token",
    "product": "Premium Subscription",
    "amount": 50000,
    "currency": 1
}

6. GET /api/confirm_payment/
data = {
    "user_token": token, 
    "token": "payment_token"
}

7. GET /api/decline_payment/
data = {
    "user_token": token, 
    "token": "payment_token"
}