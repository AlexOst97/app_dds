from dds.apps import DdsConfig
from django.urls import path
from dds.views import (StatusListAPIView,
                       StatusRetrieveAPIView,
                       StatusCreateAPIView,
                       StatusUpdateAPIView,
                       StatusDestroyAPIView,

                       TypeListAPIView,
                       TypeRetrieveAPIView,
                       TypeCreateAPIView,
                       TypeUpdateAPIView,
                       TypeDestroyAPIView,

                       CategoryListAPIView,
                       CategoryRetrieveAPIView,
                       CategoryCreateAPIView,
                       CategoryUpdateAPIView,
                       CategoryDestroyAPIView,

                       SubcategoryListAPIView,
                       SubcategoryRetrieveAPIView,
                       SubcategoryCreateAPIView,
                       SubcategoryUpdateAPIView,
                       SubcategoryDestroyAPIView,

                       CashFlowListAPIView,
                       CashFlowRetrieveAPIView,
                       CashFlowCreateAPIView,
                       CashFlowUpdateAPIView,
                       CashFlowDestroyAPIView,

                        InfoTableListAPIView,
                       )


app_name = DdsConfig.name

urlpatterns = [
    # Для Status
    path('status/', StatusListAPIView.as_view(), name='status-list'),
    path('status/<int:pk>/', StatusRetrieveAPIView.as_view(), name='status-retrieve'),
    path('status/create/', StatusCreateAPIView.as_view(), name='status-create'),
    path('status/<int:pk>/update/', StatusUpdateAPIView.as_view(), name='status-update'),
    path('status/<int:pk>/destroy/', StatusDestroyAPIView.as_view(), name='status-destroy'),

    # Для Type
    path('type/', TypeListAPIView.as_view(), name='type-list'),
    path('type/<int:pk>/', TypeRetrieveAPIView.as_view(), name='type-retrieve'),
    path('type/create/', TypeCreateAPIView.as_view(), name='type-create'),
    path('type/<int:pk>/update/', TypeUpdateAPIView.as_view(), name='type-update'),
    path('type/<int:pk>/destroy/', TypeDestroyAPIView.as_view(), name='type-destroy'),

    # Для Category
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/<int:pk>/destroy/', CategoryDestroyAPIView.as_view(), name='category-destroy'),

    # Для Subcategory
    path('subcategory/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', SubcategoryRetrieveAPIView.as_view(), name='subcategory-retrieve'),
    path('subcategory/create/', SubcategoryCreateAPIView.as_view(), name='subcategory-create'),
    path('subcategory/<int:pk>/update/', SubcategoryUpdateAPIView.as_view(), name='subcategory-update'),
    path('subcategory/<int:pk>/destroy/', SubcategoryDestroyAPIView.as_view(), name='subcategory-destroy'),

    # Для CashFlow
    path('cashflow/', CashFlowListAPIView.as_view(), name='cashflow-list'),
    path('cashflow/<int:pk>/', CashFlowRetrieveAPIView.as_view(), name='cashflow-retrieve'),
    path('cashflow/create/', CashFlowCreateAPIView.as_view(), name='cashflow-create'),
    path('cashflow/<int:pk>/update/', CashFlowUpdateAPIView.as_view(), name='cashflow-update'),
    path('cashflow/<int:pk>/destroy/', CashFlowDestroyAPIView.as_view(), name='cashflow-destroy'),

    path('table/', InfoTableListAPIView.as_view(), name='table'),
]
