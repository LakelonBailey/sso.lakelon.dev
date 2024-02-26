from django.views import View
from django.http import (
    HttpRequest,
    JsonResponse,
    HttpResponseBadRequest
)
import json
from identity.models import Client, AuthorizationCode
from accounts.serializers import AccountSerializer
from utils.jwt import create_id_token, create_access_token


MAX_CODE_USES = 5


class PublicKeyView(View):
    def get(self, request: HttpRequest):
        with open('jwtRS256.key.pub', 'r') as file:
            public_key = file.read()

        return JsonResponse({'public_key': public_key})


class AuthorizeView(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        code = data.get('code', None)
        client_id = data.get('client_id', None)
        client_secret = data.get('client_secret', None)
        if not all([code, client_id, client_secret]):
            return HttpResponseBadRequest()

        authorization_code = (
            AuthorizationCode.objects
            .filter(
                code=code
            )
            .select_related('client', 'account')
            .first()
        )

        if authorization_code is None or \
                authorization_code.uses >= MAX_CODE_USES:
            return HttpResponseBadRequest()

        authorization_code.uses += 1
        authorization_code.save()

        client: Client = authorization_code.client
        if not (
            str(client.client_id) == client_id
            and str(client.client_secret) == client_secret
        ):
            return HttpResponseBadRequest()

        if client is None:
            return HttpResponseBadRequest()

        payload = AccountSerializer(authorization_code.account).data

        return JsonResponse({
            'access_token': create_access_token(
                client.client_url,
                authorization_code.account.email,
            ),
            'id_token': create_id_token(payload)
        })
