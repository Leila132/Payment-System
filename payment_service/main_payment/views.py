from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
import requests
from django.http import HttpResponseRedirect, HttpResponse
import requests
import json
from rest_framework.permissions import IsAuthenticated

URL = 'https://app-demo.payadmit.com/api/v1/payments'

class createPaymentAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request: Request) -> Response:
        MERCHANT_PRIVATE_KEY = 'f2a1e7531f66eec765a8'
        SANDBOX_URL = 'https://business.processinprocess.com'

        payload = {
            "product": "Your Product",
            "amount": 100000,
            "currency": "NGN",
            "orderNumber": "your order number",
            "extraReturnParam": "your order id or other info",
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
            print(resp_payload)
            return HttpResponseRedirect(resp_payload['processingUrl'])
        else:
            print(resp.text)
            return HttpResponse('<html><body><span>Something gone wrong: %s</span></body></html>' % (resp.status_code))
        
    def get(self, request: Request) -> Response:
        SANDBOX_URL = 'https://business.processinprocess.com'
        MERCHANT_PRIVATE_KEY = 'f2a1e7531f66eec765a8'
        params = {
            'dateFrom': '2023-01-01',
            'dateTo': '2025-12-31',
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
            print(json.dumps(payments_list))
            return HttpResponse(json.dumps(payments_list), content_type='application/json')
        else:
            return HttpResponse('<html><body><span>Something gone wrong: %s</span></body></html>' % (resp.status_code))