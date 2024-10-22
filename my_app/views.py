from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from rest_framework.views import APIView
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0759297027'
    amount = 1
    account_reference = 'ephraim reference'
    transaction_desc = 'First ephraim mpesa integration api pay Description'
    callback_url = 'https://e9b7-2c0f-fe38-2335-dabf-2555-b99c-7f52-1c96.ngrok-free.app/daraja/stk-push'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        print(data)
        return HttpResponse("STK Push in Django👋")


class MpesaPaymentView(APIView):
    def post(self, request):
        cl = MpesaClient()
        phone_number = request.data.get('phone_number', '0759297027')
        amount = request.data.get('amount', 1)
        account_reference = request.data.get('account_reference', 'ephraim reference')
        transaction_desc = request.data.get('transaction_desc', 'First ephraim mpesa integration API pay Description')
        callback_url = 'https://e9b7-2c0f-fe38-2335-dabf-2555-b99c-7f52-1c96.ngrok-free.app/mpesa-callback/'
        
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return Response(response, status=status.HTTP_200_OK)

class StkPushCallbackView(APIView):
    def post(self, request):
        data = request.data  # Parse the incoming callback data

        print({"message": "STK Push Callback Received",
                         "data":data})
        return Response({"message": "STK Push Callback Received",
                         "data":data}, status=status.HTTP_200_OK)
