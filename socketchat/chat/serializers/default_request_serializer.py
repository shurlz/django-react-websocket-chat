from rest_framework import serializers


class DefaultIDRequestSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
