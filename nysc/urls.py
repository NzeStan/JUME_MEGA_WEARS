from django.urls import path
from .views import ProductList, ProductDetail, NyscLandingPage


urlpatterns = [
    path("nysc_landing/", NyscLandingPage.as_view(), name="nysc_landing"),
    path("product/", ProductList.as_view(), name="product_list"),
    path("nysc_detail/<int:pk>/", ProductDetail.as_view(), name="nysc_detail"),
]
