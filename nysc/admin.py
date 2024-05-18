from django.contrib import admin
from .models import Product, Measurement
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "size",
        "price",
        "available",
        "created",
        "updated",
        "type",
    ]
    list_filter = [
        "type",
        "available",
        "created",
        "updated",
    ]
    list_editable = [
        "price",
        "available",
    ]


@admin.register(Measurement)
class MeasurementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "chest",
        "shoulder",
        "sleeve_length",
        "waist",
        "thigh",
        "trouser_length",
    ]
