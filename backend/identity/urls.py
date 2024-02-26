from django.urls import path
from identity.views import AuthorizeView, PublicKeyView

urlpatterns = [
    path('public-key/', PublicKeyView.as_view()),
    path('authorize/', AuthorizeView.as_view()),
]