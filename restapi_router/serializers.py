from rest_framework import serializers
from .models import RestRouterDetails


class RestRouterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestRouterDetails
        fields = '__all__'