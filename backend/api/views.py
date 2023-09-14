"""API views"""
import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    """_summary_

    Args:
        request (HttpRequest): HttpRequest instance from Django

    Returns:
        _type_: _description_
    """
    print(request.GET)
    print(request.POST)
    body = request.body  # byte string of request.body
    data = {}
    try:
        data = json.loads(body)  # String of JSON -> Python dict
    except:
        pass

    print(data)
    print(request.headers)
    # HttpHeaders - not JSON serializable
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
