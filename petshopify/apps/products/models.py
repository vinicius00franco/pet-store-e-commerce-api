from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        "products.Category",  # Caminho correto para o app de produtos
        related_name="products",
        on_delete=models.CASCADE, # C
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
