from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from import_export.admin import ImportExportModelAdmin

CustomUser = get_user_model()


class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "nysc_call_up_number",
        "state_of_deployment",
        "is_superuser",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
