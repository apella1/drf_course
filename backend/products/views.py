"""API Views"""
# from django.http import Http404
from django.shortcuts import get_object_or_404

# from django.http import Http404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    """_summary_

    Args:
        generics (_type_): _description_
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """_summary_

    Args:
        generics (_type_): _description_
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer = self.request.user
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)


# class ProductListAPIView(generics.ListAPIView):
#     """_summary_

#     Args:
#         generics (_type_): _description_
#     """

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# also possible to assign the class
# product_detail_api_view = ProductDetailAPIView.as_view()

# Illustrating function-based views


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  # PUT -> update, DESTROY -> delete

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            # many=False is the default
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # Else isn't necessary in this case. Leaving it in for clarity
        else:
            # list view
            query_set = Product.objects.all()
            query_set = ProductSerializer(query_set, many=True).data
            return Response(query_set)
            # get data -> list view or detail view
            # url_args
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "Data is not valid"}, status=400)
