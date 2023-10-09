"""Product serializers"""

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer
    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
    """

    # ModelSerializer assumes an instance(saved data) is attached to the model

    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # HyperlinkedIdentityField can only be used
    # within the ModelSerializer class
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    # email = serializers.EmailField(write_only=True)

    class Meta:
        """_summary_"""

        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     # instance.title = validated_data.get("title")
    #     # return instance
    #     email = validated_data.pop("email")
    #     print(email)
    #     return super().update(instance, validated_data)

    def get_my_discount(self, obj):
        """Getting the my_discount property"""
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    # * using SerializerMethodField for this
    # * i.e url = serializers.SerializerMethodField(read_only=True)

    # def get_url(self, obj):
    #     """Getting the url of an individual product"""
    #     request = self.context.get("request")

    #     return (
    #         None
    #         if request is None
    #         else reverse(
    #               viewname="product-detail",
    #               kwargs={"pk": obj.pk},
    #               request=request
    #           )

    # return f"/api/products/{obj.pk}"

    def get_edit_url(self, obj):
        """Getting the url of an individual product's update page"""
        request = self.context.get("request")
        return (
            None
            if request is None
            else reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
        )
