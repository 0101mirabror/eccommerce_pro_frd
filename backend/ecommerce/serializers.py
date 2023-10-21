from rest_framework import serializers
from .models import Product, Order

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'firstname', 'lastname']
