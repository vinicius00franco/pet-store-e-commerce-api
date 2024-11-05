from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import ProductFilter
from .pagination import DynamicPageNumberPagination
from .serializers import ProductSerializer
from .services.product_service import (
    create_product,
    get_product,
    update_product,
    delete_product,
)
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DynamicPageNumberPagination
    search_fields = ["name", "description"]
    ordering_fields = ["price", "name"]

    # Custom Action for Create
    @action(detail=False, methods=["post"], url_path="create")
    def custom_create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = create_product(serializer.validated_data)
            return Response(
                ProductSerializer(product).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom Action for Retrieve
    @action(detail=False, methods=["get"], url_path="retrieve")
    def retrieve_all(self, request):
        """Retrieve all available products with automatic filtering, ordering, and pagination."""
        # Apply all filters, search, and ordering automatically
        queryset = self.filter_queryset(self.get_queryset())

        # Automatically paginate the queryset if pagination is enabled
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If no pagination, just serialize and return the data
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Custom Action for Update
    @action(detail=True, methods=["put", "patch"], url_path="update")
    def custom_update(self, request, pk=None):
        product = get_product(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            updated_product = update_product(product, serializer.validated_data)
            return Response(
                ProductSerializer(updated_product).data, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom Action for Delete (Logical Delete)
    @action(detail=True, methods=["delete"], url_path="delete")
    def custom_delete(self, request, pk=None):
        product = get_product(pk)
        delete_product(product)
        return Response(
            {"status": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
