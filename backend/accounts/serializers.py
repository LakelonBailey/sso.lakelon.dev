from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    roles = serializers.ListField(child=serializers.CharField())
