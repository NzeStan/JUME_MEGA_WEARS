from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "size",
        "price",
        "available",
        "created",
        "updated",
    ]
    list_filter = [
        "available",
        "created",
        "updated",
    ]
    list_editable = [
        "price",
        "available",
    ]
