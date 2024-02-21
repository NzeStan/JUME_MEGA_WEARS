from django.urls import path
from .views import (
    Photos,
    DetailPhotoView,
    HomeCreateView,
    ContactDeleteView,
    NzeStan,
    Inspos,
    DetailInspoView,
    Videos,
    DetailVideoView,
    AboutUsView,
    ContactUsView,
)

urlpatterns = [
    path("", HomeCreateView.as_view(), name="home"),
    path("photo/", Photos.as_view(), name="photo"),
    path("detail_photo/<int:pk>/", DetailPhotoView.as_view(), name="detail_photo"),
    path("inspo/", Inspos.as_view(), name="inspo"),
    path("detail_inspo/<int:pk>/", DetailInspoView.as_view(), name="detail_inspo"),
    path("video/", Videos.as_view(), name="video"),
    path("detail_video/<int:pk>/", DetailInspoView.as_view(), name="detail_video"),
    path("nze_stan/", NzeStan.as_view(), name="nze_stan"),
    path(
        "contact_us_delete/<int:pk>",
        ContactDeleteView.as_view(),
        name="contact_us_delete",
    ),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
]
