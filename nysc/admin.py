from django.contrib import admin
from .models import Product, Measurement, Event
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


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "end_datetime",
    ]
