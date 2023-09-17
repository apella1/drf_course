"""API views"""
import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from products.models import Product


def api_home(request, *args, **kwargs):
    """_summary_

    Args:
        request (HttpRequest): HttpRequest instance from Django

    Returns:
        _type_: _description
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["content", "title", "price"])
        # model instance (model_data) -> Python dict -> JSON to client
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str,
                        headers={"content-type": "application/json"})
