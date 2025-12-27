# apps/products/services.py
from django.core.exceptions import ValidationError
from .models import Product

class ProductService:

    @staticmethod
    def list_products(params=None):
        qs = Product.objects.all()
        # Aqui você pode optar por aplicar filtros no service se precisar
        # mas o padrão de mercado é aplicar via filter_backends na ViewSet.
        return qs

    @staticmethod
    def get_product(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product not found")

    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)

    @staticmethod
    def update_product(product, data):
        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return product

    @staticmethod
    def delete_product(product):
        if product.quantity > 0:
            raise ValidationError("Cannot delete product with stock")
        product.delete()
