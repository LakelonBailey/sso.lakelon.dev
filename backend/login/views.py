from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.views import View
from accounts.models import Account
from identity.models import AuthorizationCode, Client
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

        client = Client.objects.filter(client_id=client_id).first()
        if client is None:
            return HttpResponseBadRequest()

        account = Account.objects.filter(email=email).first()
        if account is None:
            return bad_username_or_password()

        if not account.check_password(password):
            return bad_username_or_password()

        return JsonResponse({
            'success': True,
            'code': AuthorizationCode.objects.create(
                client=client,
                account=account,
            ).code
        })
