from django.urls import path
from . import views


urlpatterns = [
    path("create_orders/", views.order_create, name="order_create"),
    path(
        "admin/order/<int:order_id>/pdf/", views.admin_order_pdf, name="admin_order_pdf"
    ),
    path("update_order/<int:pk>", views.UpdateOrderView.as_view(), name="update_order"),
    path("state_aba/", views.state_aba, name="state_aba"),
]
