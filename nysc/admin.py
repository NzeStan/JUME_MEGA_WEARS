from django.contrib import admin
from .models import Product, Measurement


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


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "chest",
        "shoulder",
        "sleeve_length",
        "waist",
        "thigh",
        "trouser_length",
    ]
