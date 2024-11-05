from rest_framework import serializers
from .models import Category, Product
from .models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


class ProductSerializer(serializers.ModelSerializer):
    # Para operações de leitura, exibir a categoria detalhada
    category = CategorySerializer(read_only=True)
    # Para operações de escrita, permitir definir a categoria via ID
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "stock",
            "image",
            "available",
            "category",
            "category_id",
        )
