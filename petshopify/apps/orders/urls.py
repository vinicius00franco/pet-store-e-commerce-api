from django.urls import path
from .views import OrderViewSet


order_create = OrderViewSet.as_view({"post": "create_order"})

urlpatterns = [
    path("create", order_create, name="order-create"),
]
