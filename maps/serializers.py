from rest_framework import serializers
from .models import City, Gu, Dong

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class GuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gu
        fields = '__all__'

class DongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dong
        fields = '__all__'
