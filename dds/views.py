from rest_framework import generics
from dds.models import Status, Type, Category, Subcategory, CashFlow
from dds.serializers import (StatusSerializers,
                             TypeSerializers,
                             CategorySerializers,
                             SubcategorySerializers,
                             CashFlowSerializers)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render


# Для Status
class StatusListAPIView(generics.ListAPIView):
    serializer_class = StatusSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_list.html"
    context_object_name = "statuses"

    def get(self, request):
        obj = Status.objects.all()
        return Response({"statuses": obj})


class StatusRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_retrieve.html"
    context_object_name = "status"

    def get(self, request, pk):
        obj = Status.objects.get(pk=pk)
        serializer = StatusSerializers(obj)
        return Response({"serializer": serializer, "status": obj})


class StatusCreateAPIView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:status-list")
        return Response({"serializer": serializer})


class StatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_update.html"

    def get(self, request, pk):
        obj = Status.objects.get(pk=pk)
        serializer = StatusSerializers(obj)
        return Response({"serializer": serializer, "status": obj})

    def post(self, request, pk):
        obj = Status.objects.get(pk=pk)
        serializer = StatusSerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:status-list")
        return Response({"serializer": serializer})


class StatusDestroyAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_delete.html"

    def get(self, request, pk):
        obj = Status.objects.get(pk=pk)
        serializer = StatusSerializers(obj)
        return Response({"serializer": serializer, "status": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("dds:status-list")


# Для Type
class TypeListAPIView(generics.ListAPIView):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()


class TypeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()


class TypeCreateAPIView(generics.CreateAPIView):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()


class TypeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()


class TypeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()


# Для Category
class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


# Для Subcategory
class SubcategoryListAPIView(generics.ListAPIView):
    serializer_class = SubcategorySerializers
    queryset = Subcategory.objects.all()


class SubcategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubcategorySerializers
    queryset = Subcategory.objects.all()


class SubcategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = SubcategorySerializers
    queryset = Subcategory.objects.all()


class SubcategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubcategorySerializers
    queryset = Subcategory.objects.all()


class SubcategoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubcategorySerializers
    queryset = Subcategory.objects.all()


# Для CashFlow
class CashFlowListAPIView(generics.ListAPIView):
    serializer_class = CashFlowSerializers
    queryset = CashFlow.objects.all()


class CashFlowRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CashFlowSerializers
    queryset = CashFlow.objects.all()


class CashFlowCreateAPIView(generics.CreateAPIView):
    serializer_class = CashFlowSerializers
    queryset = CashFlow.objects.all()


class CashFlowUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CashFlowSerializers
    queryset = CashFlow.objects.all()


class CashFlowDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CashFlowSerializers
    queryset = CashFlow.objects.all()
