from django.urls import path, include

urlpatterns = [
    path('api/', include('main.api_urls'))
]
