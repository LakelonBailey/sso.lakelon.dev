from django.contrib import admin
from identity.models import Client


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['client_name', 'client_url']
    readonly_fields = ['client_id', 'client_secret']


admin.site.register(Client, ClientAdmin)
