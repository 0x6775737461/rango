from app.models import Region, Fruits
from rest_framework import serializers

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = ['id', 'name', 'origin']
