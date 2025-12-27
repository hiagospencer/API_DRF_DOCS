# apps/products/filters.py
import django_filters
from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    # Preço
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    exact_price = filters.NumberFilter(field_name="price")

    # Nome
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    name_exact = filters.CharFilter(field_name="name", lookup_expr="iexact")
    name_starts = filters.CharFilter(field_name="name", lookup_expr="istartswith")

    # Estoque
    in_stock = filters.BooleanFilter(field_name="in_stock")
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr="gte")
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr="lte")

    # Datas
    created_after = filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_before = filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    # Ordenação customizada (opcional)
    ordering = filters.OrderingFilter(
        fields=(
            ("price", "price"),
            ("created_at", "created_at"),
            ("name", "name"),
            ("quantity", "quantity"),
        )
    )

    class Meta:
        model = Product
        fields = [
            "in_stock",
            "price",
            "quantity",
        ]
