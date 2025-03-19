import requests
from django.conf import settings
import json
from django.http import HttpResponseRedirect, HttpResponse

def get_user_from_token(token_key):
    auth_api_url = "http://127.0.0.1:8000/api/verify-token/"
    response = requests.post(auth_api_url, json={"token": token_key})
    if response.status_code == 200:
        return response.json()
    return None

def create_payment(payment_data, user):
    MERCHANT_PRIVATE_KEY = user['user_token_api']
    SANDBOX_URL = settings.SANDBOX_URL

    payload = {
        "product": payment_data['product'],
        "amount": payment_data['amount'],
        "currency": payment_data['currency'],
        "orderNumber": payment_data['orderNumber'],
        "customer": {
            "name": user['username']
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % (MERCHANT_PRIVATE_KEY)
    }

    resp = requests.post('%s/api/v1/payments' % (SANDBOX_URL), json=payload, headers=headers)

    if resp.status_code == 200:
        resp_payload = json.loads(resp.text)
        #print(resp_payload)
        return HttpResponseRedirect(resp_payload['processingUrl'])
    else:
        #print(resp.text)
        return HttpResponse('<html><body><span>Something gone wrong: %s</span></body></html>' % (resp.status_code))