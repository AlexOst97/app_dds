from rest_framework import serializers
from dds.models import Status, Type, Category, Subcategory, CashFlow


class StatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"


class TypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SubcategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = "__all__"


class CashFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = CashFlow
        fields = "__all__"
        read_only_fields = ("created_at",)
