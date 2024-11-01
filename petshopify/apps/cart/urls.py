from django.urls import path
from .views import CartViewSet

cart_list = CartViewSet.as_view({"get": "retrieve"})
cart_add_item = CartViewSet.as_view({"post": "add_item"})
cart_update_item = CartViewSet.as_view({"put": "update_item"})
cart_remove_item = CartViewSet.as_view({"delete": "remove_item"})


urlpatterns = [
    path("", cart_list, name="cart-list"),
    path("add", cart_add_item, name="cart-add-item"),
    path("update/<int:pk>", cart_update_item, name="cart-update-item"),
    path("remove/<int:pk>", cart_remove_item, name="cart-remove-item"),
]
