"""Normally viewsets would be placed in the views.py file """

from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_
    Methods: get -> list, get -> retrieve single, post, put, patch, delete
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default


class ProductGenericViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """_summary_

    Args:
        viewsets (_type_): _description_
    Methods: get -> list, get -> retrieve
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
