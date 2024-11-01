from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .pagination import DynamicPageNumberPagination


# Home view padrão do Django
def home(request):
    return HttpResponse("<h1>Welcome to PetShopify API!</h1>")


# View para listar produtos com filtros, busca e paginação
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DynamicPageNumberPagination

    search_fields = ["name", "description"]
    ordering_fields = ["price", "name"]


# View para detalhar produto específico
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
