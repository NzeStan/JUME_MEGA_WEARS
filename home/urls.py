from django.urls import path
from .views import (
    Photos,
    DetailPhotoView,
    HomeCreateView,
    ContactDeleteView,
    NzeStan,
    Inspos,
    DetailInspoView,
    AboutUsView,
    ContactUsView,
)

urlpatterns = [
    path("", HomeCreateView.as_view(), name="home"),
    path("photo/", Photos.as_view(), name="photo"),
    path("detail_photo/<uuid:pk>/", DetailPhotoView.as_view(), name="detail_photo"),
    path("inspo/", Inspos.as_view(), name="inspo"),
    path("detail_inspo/<uuid:pk>/", DetailInspoView.as_view(), name="detail_inspo"),
    path("nze_stan/", NzeStan.as_view(), name="nze_stan"),
    path(
        "contact_us_delete/<uuid:pk>",
        ContactDeleteView.as_view(),
        name="contact_us_delete",
    ),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
]
