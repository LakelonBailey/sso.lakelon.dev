# Django Imports
from django.db import models
from uuid import uuid4
from main.models import BaseClass
import random
import string


def default_client_secret():
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(64)
    )


class Client(BaseClass):
    client_name = models.CharField(max_length=100, null=True)
    client_url = models.CharField(max_length=100, null=True)

    client_id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False
    )

    client_secret = models.CharField(
        default=default_client_secret,
        max_length=64,
        null=False,
        unique=True,
        editable=False,
    )

    authorized_accounts = models.ManyToManyField(
        'accounts.Account',
        related_name='authorized_clients'
    )

    def __str__(self):
        return self.client_url


class AuthorizationCode(BaseClass):
    account = models.ForeignKey(
        'accounts.Account',
        null=True,
        on_delete=models.CASCADE,
        related_name='authorization_codes'
    )

    client = models.ForeignKey(
        'identity.Client',
        null=True,
        on_delete=models.CASCADE,
        related_name='authorization_codes'
    )

    code = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False
    )

    uses = models.IntegerField(default=0)
