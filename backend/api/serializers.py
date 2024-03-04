from rest_framework import serializers
from .models import *

class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = ['id', 'name', 'hours', 'avg_rating', 'web', 'address', 'location', 'image', 'closing', 'low_price']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'day', 'available', 'unavailable', 'avg_rating', 'meat', 'vegetarian', 'soup', 'canteen_id']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'menu_id', 'stars', 'body', 'created_at']