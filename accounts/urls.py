from django.urls import path
from .views import (
    Update_User_Detail,
)


urlpatterns = [
    path(
        "update_user/<int:pk>/",
        Update_User_Detail.as_view(),
        name="update_user",
    ),
]
