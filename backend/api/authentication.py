"""API authentication module"""
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    """_summary_

    Args:
        BaseTokenAuth (_type_): _description_
    """
    keyword = "Bearer"
