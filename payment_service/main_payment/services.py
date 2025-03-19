import requests
from django.conf import settings
import json
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime

def get_user_from_token(token_key):
    auth_api_url = "http://127.0.0.1:8000/api/verify-token/"
    response = requests.post(auth_api_url, json={"token": token_key})
    if response.status_code == 200:
        return response.json()
    return None

def check_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create_payment(payment_data, user):
    MERCHANT_PRIVATE_KEY = user['user_token_api']
    SANDBOX_URL = settings.SANDBOX_URL

    payload = {
        "product": payment_data['product'],
        "amount": payment_data['amount'],
        "currency": payment_data['currency'],

        "customer": {
            "email": "yourmail@gmail.com"
        }

    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % (MERCHANT_PRIVATE_KEY)
    }

    resp = requests.post('%s/api/v1/payments' % (SANDBOX_URL), json=payload, headers=headers)
    if resp.status_code == 200:
        resp_payload = json.loads(resp.text)
        #return HttpResponseRedirect(resp_payload['processingUrl'])
        return resp_payload
    else:
        #print(resp.text)
        return HttpResponse('<html><body><span>Something gone wrong: %s</span></body></html>' % (resp.status_code))
    
def get_payments_list(payment_data, user):
    MERCHANT_PRIVATE_KEY = user['user_token_api']
    SANDBOX_URL = settings.SANDBOX_URL
    params = {
        'dateFrom': payment_data['date_start'],
        'dateTo': payment_data['date_end'],
        'page': 1,
        'perPage': 20
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % (MERCHANT_PRIVATE_KEY)
    }

    resp = requests.get('%s/api/v1/payments' % (SANDBOX_URL), params=params, headers=headers)

    if resp.status_code == 200:
        payments_list = json.loads(resp.text)
        return HttpResponse(json.dumps(payments_list), content_type='application/json')
    else:
        return HttpResponse('<html><body><span>Something gone wrong: %s</span></body></html>' % (resp.status_code))