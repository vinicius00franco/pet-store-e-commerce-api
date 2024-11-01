# products/filters.py

from django_filters import rest_framework as filters
from .models import Product, Category


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["name", "description", "min_price", "max_price", "category"]
