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
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)

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

    def get_url(self, obj):
        """Getting the url of an individual product"""
        request = self.context.get("request")

        return (
            None
            if request is None
            else reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
        )

        # return f"/api/products/{obj.pk}"

    def get_edit_url(self, obj):
        """Getting the url of an individual product's update page"""
        request = self.context.get("request")
        return (
            None
            if request is None
            else reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
        )
