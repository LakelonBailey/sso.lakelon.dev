# Django Imports
from django.db.models import UUIDField, CharField, ManyToManyField
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
    client_name = CharField(max_length=100, null=True)
    client_url = CharField(max_length=100, null=True)

    client_id = UUIDField(
        default=uuid4,
        unique=True,
        editable=False
    )

    client_secret = CharField(
        default=default_client_secret,
        max_length=64,
        null=False,
        unique=True,
        editable=False,
    )

    authorized_accounts = ManyToManyField(
        'accounts.Account',
        related_name='authorized_clients'
    )

    def __str__(self):
        return self.client_url
