from django.contrib import admin
from dds.models import Status, Type, Category, Subcategory, CashFlow





@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")