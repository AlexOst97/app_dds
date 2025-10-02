from rest_framework import generics
from dds.models import Status, Type, Category, Subcategory, CashFlow
from dds.serializers import (StatusSerializers,
                             TypeSerializers,
                             CategorySerializers,
                             SubcategorySerializers,
                             CashFlowSerializers)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import redirect


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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_list.html"
    context_object_name = "types"

    def get(self, request):
        obj = Type.objects.all()
        return Response({"types": obj})


class TypeRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_retrieve.html"
    context_object_name = "type"

    def get(self, request, pk):
        obj = Type.objects.get(pk=pk)
        serializer = TypeSerializers(obj)
        return Response({"serializer": serializer, "type": obj})


class TypeCreateAPIView(generics.CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:type_list")
        return Response({"serializer": serializer})


class TypeUpdateAPIView(generics.UpdateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_update.html"

    def get(self, request, pk):
        obj = Type.objects.get(pk=pk)
        serializer = TypeSerializers(obj)
        return Response({"serializer": serializer, "type": obj})

    def post(self, request, pk):
        obj = Type.objects.get(pk=pk)
        serializer = TypeSerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:type-list")
        return Response({"serializer": serializer})


class TypeDestroyAPIView(generics.DestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_delete.html"

    def get(self, request, pk):
        obj = Type.objects.get(pk=pk)
        serializer = TypeSerializers(obj)
        return Response({"serializer": serializer, "type": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("dds:type-list")


# Для Category
class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_list.html"
    context_object_name = "categories"

    def get(self, request):
        obj = Category.objects.all()
        return Response({"categories": obj})


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_retrieve.html"
    context_object_name = "category"

    def get(self, request, pk):
        obj = Category.objects.get(pk=pk)
        serializer = CategorySerializers(obj)
        return Response({"serializer": serializer, "category": obj})


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:category-list")
        return Response({"serializer": serializer})


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_update.html"

    def get(self, request, pk):
        obj = Category.objects.get(pk=pk)
        serializer = CategorySerializers(obj)
        return Response({"serializer": serializer, "category": obj})

    def post(self, request, pk):
        obj = Category.objects.get(pk=pk)
        serializer = CategorySerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:category-list")
        return Response({"serializer": serializer})

class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_delete.html"

    def get(self, request, pk):
        obj = Category.objects.get(pk=pk)
        serializer = CategorySerializers(obj)
        return Response({"serializer": serializer, "category": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("dds:category-list")


# Для Subcategory
class SubcategoryListAPIView(generics.ListAPIView):
    serializer_class = SubcategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_list.html"
    context_object_name = "subcategories"

    def get(self, request):
        obj = Subcategory.objects.all()
        return Response({"subcategories": obj})


class SubcategoryRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_retrieve.html"
    context_object_name = "subcategory"

    def get(self, request, pk):
        obj = Subcategory.objects.get(pk=pk)
        serializer = SubcategorySerializers(obj)
        return Response({"serializer": serializer, "subcategory": obj})


class SubcategoryCreateAPIView(generics.CreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        categories = Category.objects.all()
        return Response({
            "serializer": serializer,
            "categories": categories
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:subcategory-list")
        return Response({"serializer": serializer})


class SubcategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_update.html"

    def get(self, request, pk):
        obj = Subcategory.objects.get(pk=pk)
        categories = Category.objects.all()
        serializer = SubcategorySerializers(obj)
        return Response({
            "serializer": serializer,
            "subcategory": obj,
            "categories": categories
        })

    def post(self, request, pk):
        obj = Subcategory.objects.get(pk=pk)
        serializer = SubcategorySerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:subcategory-list")
        return Response({"serializer": serializer})


class SubcategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_delete.html"

    def get(self, request, pk):
        obj = Subcategory.objects.get(pk=pk)
        serializer = SubcategorySerializers(obj)
        return Response({"serializer": serializer, "subcategory": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("dds:subcategory-list")


# Для CashFlow
class CashFlowListAPIView(generics.ListAPIView):
    serializer_class = CashFlowSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cashflow_list.html"
    context_object_name = "cashflows"

    def get(self, request):
        obj = CashFlow.objects.all()
        return Response({"cashflows": obj})


class CashFlowRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cashflow_retrieve.html"
    context_object_name = "cashflow"

    def get(self, request, pk):
        obj = CashFlow.objects.get(pk=pk)
        serializer = CashFlowSerializers(obj)
        return Response({"serializer": serializer, "cashflow": obj})


class CashFlowCreateAPIView(generics.CreateAPIView):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cashflow_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        statuses = Status.objects.all()
        types = Type.objects.all()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        return Response({
            "serializer": serializer,
            "statuses": statuses,
            "types": types,
            "categories": categories,
            "subcategories": subcategories,
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:cashflow-list")
        return Response({"serializer": serializer})


class CashFlowUpdateAPIView(generics.UpdateAPIView):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cashflow_update.html"

    def get(self, request, pk):
        obj = CashFlow.objects.get(pk=pk)
        serializer = CashFlowSerializers(obj)
        statuses = Status.objects.all()
        types = Type.objects.all()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        return Response({
            "serializer": serializer,
            "cashflow": obj,
            "statuses": statuses,
            "types": types,
            "categories": categories,
            "subcategories": subcategories,
        })

    def post(self, request, pk):
        obj = CashFlow.objects.get(pk=pk)
        serializer = CashFlowSerializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("dds:cashflow-list")
        return Response({"serializer": serializer})


class CashFlowDestroyAPIView(generics.DestroyAPIView):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_delete.html"

    def get(self, request, pk):
        obj = CashFlow.objects.get(pk=pk)
        serializer = CashFlowSerializers(obj)
        return Response({"serializer": serializer, "subcategory": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("dds:subcategory-list")


# InfoTable
class InfoTableListAPIView(generics.ListAPIView):
    serializer_class = CashFlowSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "table.html"
    context_object_name = "objects"

    def get(self, request):
        queryset = CashFlow.objects.all()

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        status = request.GET.get('status')
        type_filter = request.GET.get('type')
        category = request.GET.get('category')
        subcategory = request.GET.get('subcategory')

        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)
        if status:
            queryset = queryset.filter(status=status)
        if type_filter:
            queryset = queryset.filter(type=type_filter)
        if category:
            queryset = queryset.filter(category_id=category)
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)

        status_choices = Status.objects.all()
        type_choices = Type.objects.all()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()

        filters = {
            'date_from': date_from,
            'date_to': date_to,
            'status': status,
            'type': type_filter,
            'category': category,
            'subcategory': subcategory,
        }

        return Response({
            "cashflows": queryset,
            "status_choices": status_choices,
            "type_choices": type_choices,
            "categories": categories,
            "subcategories": subcategories,
            "filters": filters
        })