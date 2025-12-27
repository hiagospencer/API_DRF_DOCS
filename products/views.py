# apps/products/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .permissions import IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filterset_class = ProductFilter
    search_fields = ["name"]
    ordering_fields = ["price", "created_at", "name"]
    ordering = ["-created_at"]  # padrão
