from rest_framework import serializers

from api.models import MmallCart, MmallCategory, MmallOrder, MmallOrderItem, MmallPayInfo, MmallProduct, MmallShipping, MmallUser


class MmallCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallCart
        fields = "__all__"


class MmallCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallCategory
        fields = "__all__"


class MmallOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallOrder
        fields = "__all__"


class MmallOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallOrderItem
        fields = "__all__"


class MmallPayInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallPayInfo
        fields = "__all__"


class MmallProductSerializer(serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source="category_id")
    mainImage = serializers.CharField(source="main_image")
    subImages = serializers.CharField(source="sub_images")

    class Meta:
        model = MmallProduct
        fields = "__all__"


class MmallShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallShipping
        fields = "__all__"


class MmallUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmallUser
        fields = "__all__"
