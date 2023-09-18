"""API views"""
# from django.forms.models import model_to_dict

# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """DRF API view - created with the api_view decorator

    Args:
        request (HttpRequest): HttpRequest instance from Django
        *args () :
        **kwargs () :

    Returns:
        _type_: _description
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # similar to pure Django's forms.save()
        # print(instance)
        return Response(serializer.data)
