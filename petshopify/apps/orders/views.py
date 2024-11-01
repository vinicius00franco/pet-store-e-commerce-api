from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.products.models import Product


from apps.cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create_order(self, request):
        items_data = request.data.get("items", [])
        total_price = sum(item["price"] * item["quantity"] for item in items_data)
        order = Order.objects.create(user=request.user, total_price=total_price)

        # Criação dos itens do pedido com base nos IDs dos produtos
        for item_data in items_data:
            product = get_object_or_404(Product, id=item_data["productId"])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data["quantity"],
                price=item_data["price"],
            )

        # Retorno da resposta com o pedido criado usando OrderSerializer
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
