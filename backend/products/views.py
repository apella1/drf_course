"""API Views"""
from api.mixins import StaffEditorPermissionMixin
from django.shortcuts import get_object_or_404

# from django.http import Http404
from rest_framework import generics, mixins
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


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    """Class-based view allowing for creating and listing of products
    The allowed methods for the view are POST and GET

    Args:
        generics (_type_): _description_
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # * For function-based views, decorators provide similar functionalities
    # * the authentication classes are provided as defaults
    # * in the settings.py file
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,
    # ]
    # ordering of the permission matching is important

    def perform_create(self, serializer):
        # serializer = self.request.user
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    """_summary_

    Args:
        generics (_type_): _description_
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    """_summary_

    Args:
        generics (_type_): _description_
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        """Deleting a product

        Args:
            instance (_type_): _description_
        """
        super().perform_destroy(instance)


class ProductMixinsView(
    StaffEditorPermissionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """_summary_

    Args:
        mixins (_type_): _description_
        generics (_type_): _description_

    Returns:
        _type_: _description_
    """

    # todo test out authentication and permissions for the mixins view

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # RetrieveModelMixin is the one concerned with the field
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # The list method is coming from the ListModelMixin class
        # print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
