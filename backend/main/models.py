# Django Imports
from django.db.models import Model, DateTimeField, UUIDField
from uuid import uuid4


class BaseClass(Model):
    uuid = UUIDField(
        default=uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    created_at = DateTimeField(null=True, auto_now_add=True)

    class Meta:
        abstract = True
