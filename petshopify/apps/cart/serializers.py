from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField(source="get_total_price")

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "created_at"]
