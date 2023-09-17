"""API views"""
# from django.forms.models import model_to_dict

# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API view - created with the api_view decorator

    Args:
        request (HttpRequest): HttpRequest instance from Django
        *args () :
        **kwargs () :

    Returns:
        _type_: _description
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(
        #     instance, fields=["content", "title", "price", "sale_price"]
        # )
        # model instance (model_data) -> Python dict -> JSON to client
        data = ProductSerializer(instance).data
    return Response(data)
