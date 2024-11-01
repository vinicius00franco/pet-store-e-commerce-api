from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.products.models import Product 
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def add_item(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=request.data.get("product_id"))
        quantity = int(request.data.get("quantity", 1))
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["put"])
    def update_item(self, request, pk=None):
        item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        item.quantity = request.data.get("quantity", item.quantity)
        item.save()
        return Response(CartItemSerializer(item).data)

    @action(detail=True, methods=["delete"])
    def remove_item(self, request, pk=None):
        item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
