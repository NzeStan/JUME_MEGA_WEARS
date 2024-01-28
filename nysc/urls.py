from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    NyscLandingPage,
    CreateMeasurementView,
    UpdateMeasurementView,
)


urlpatterns = [
    path("nysc_landing/", NyscLandingPage.as_view(), name="nysc_landing"),
    path("product/", ProductList.as_view(), name="product_list"),
    path("nysc_detail/<int:pk>/", ProductDetail.as_view(), name="nysc_detail"),
    path(
        "create_measurement/",
        CreateMeasurementView.as_view(),
        name="create_measurement",
    ),
    path(
        "update_measurement/<int:pk>/",
        UpdateMeasurementView.as_view(),
        name="update_measurement",
    ),
]
