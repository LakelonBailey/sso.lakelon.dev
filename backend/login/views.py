from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views import View
from accounts.models import Account
import json
import os

secret = os.environ['SECRET_KEY']


class LoginView(View):
    def post(self, request: HttpRequest):
        def bad_username_or_password():
            return JsonResponse({
                'success': False,
                'reason': 'Invalid username or password'
            })

        data = json.loads(request.body)
        email = data.get('email', None)
        password = data.get('password', None)
        client_id = data.get('client_id', None)
        if any([item is None for item in [email, password, client_id]]):
            return HttpResponseBadRequest()

        account = Account.objects.filter(email=email).first()
        if account is None:
            return bad_username_or_password()

        if not account.check_password(password):
            return bad_username_or_password()

        return JsonResponse({
            'success': True,
            'code': account.generate_code(client_id)
        })
