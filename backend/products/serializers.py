"""Product serializers"""

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """_summary_
    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
    """

    # ModelSerializer assumes an instance(saved data) is attached to the model

    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """_summary_"""

        model = Product
        fields = ["title", "content", "price", "sale_price", "my_discount"]

    def get_my_discount(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
