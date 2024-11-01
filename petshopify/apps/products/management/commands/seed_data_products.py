from django.core.management.base import BaseCommand
from apps.products.models import Category, Product  # ajuste o caminho se necessário
from decimal import Decimal
import random


class Command(BaseCommand):
    help = "Cria 100 dados de seed realistas para um e-commerce de acessórios para pets"

    def handle(self, *args, **kwargs):
        # Criar categorias de exemplo para pet shop
        category_names = [
            "Brinquedos",
            "Ração",
            "Acessórios",
            "Higiene",
            "Camas e Almofadas",
        ]
        categories = []

        for name in category_names:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={"description": f"Categoria de {name} para seu pet"},
            )
            categories.append(category)

        # Dados de exemplo para diferentes tipos de produtos de pets
        product_names = [
            "Osso de Brinquedo",
            "Bolinha para Gatos",
            "Ração Premium",
            "Comedouro Inteligente",
            "Cama Macia",
            "Shampoo para Pets",
            "Coleira com Identificação",
            "Arranhador de Sisal",
            "Tapete Higiênico",
            "Porta-Ração Hermético",
        ]

        product_descriptions = [
            "Produto de alta qualidade e durabilidade.",
            "Ideal para todos os tipos de pets.",
            "Seguro e confortável para o seu pet.",
            "Item essencial para o bem-estar do seu animal.",
            "Produto recomendado por veterinários.",
            "Desenvolvido com materiais resistentes e seguros.",
            "Prático e fácil de usar no dia-a-dia.",
            "Projetado para satisfazer as necessidades do seu pet.",
            "Fabricado com materiais ecológicos e duráveis.",
            "Perfeito para garantir a diversão e conforto do seu pet.",
        ]

        # Gerar 100 produtos
        for i in range(100):
            Product.objects.create(
                category=random.choice(categories),
                name=f"{random.choice(product_names)} {i+1}",  # Nome único
                description=random.choice(product_descriptions),
                price=Decimal(random.uniform(10, 500)).quantize(Decimal("0.01")),
                stock=random.randint(5, 100),
                available=random.choice([True, False]),
            )

        self.stdout.write(
            self.style.SUCCESS(
                "100 produtos de seed criados com sucesso para o e-commerce de pets!"
            )
        )
