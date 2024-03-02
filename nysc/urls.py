from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    NyscLandingPage,
    CreateMeasurementView,
    UpdateMeasurementView,
    EventDetailView,
    get_event_data,
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
    path("events/", EventDetailView.as_view(), name="event_detail"),
    path("get_event_data/", get_event_data, name="get_event_data"),
]
