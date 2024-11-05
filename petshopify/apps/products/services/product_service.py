from django.shortcuts import get_object_or_404
from django.db import transaction
from ..models import Product


def create_product(validated_data):
    """Create a new product with validated data."""
    with transaction.atomic():
        product = Product.objects.create(**validated_data)
    return product


def get_product(pk):
    """Retrieve a single product by primary key if available."""
    return get_object_or_404(Product, pk=pk, available=True)


def update_product(product, validated_data):
    """Update an existing product with validated data."""
    with transaction.atomic():
        for attr, value in validated_data.items():
            setattr(product, attr, value)
        product.save()
    return product


def delete_product(product):
    """Perform a logical delete by setting 'available' to False."""
    with transaction.atomic():
        product.available = False
        product.save()
