from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


def order_pdf(obj):
    url = reverse("admin_order_pdf", args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


order_pdf.short_description = "Invoice"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "paid",
        "created",
        "updated",
        order_pdf,
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
