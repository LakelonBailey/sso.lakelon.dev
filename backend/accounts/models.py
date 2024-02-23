from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField
from utils.jwt import create_token


class Account(AbstractUser):
    roles = ArrayField(CharField(max_length=100, null=True), default=list)

    def __str__(self):
        return self.username

    def generate_code(self, client_id: str) -> str:
        payload = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'roles': self.roles,
            'client_id': client_id,
        }

        return create_token(payload)
