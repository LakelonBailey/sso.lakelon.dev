from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField


class Account(AbstractUser):
    roles = ArrayField(CharField(max_length=100, null=True), default=list)

    def __str__(self):
        return self.username
