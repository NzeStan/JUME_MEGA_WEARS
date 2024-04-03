from django.contrib import admin
from .models import Contact, Photo, Inspo
from import_export.admin import ImportExportModelAdmin


# Override the default site header
admin.site.site_header = "JUME MEGA WEARS & ACCESSORIES"


class PhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "image",
    )


class InspoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "inspo",
    )


class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "message",
    )


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Inspo, InspoAdmin)
admin.site.register(Contact, ContactAdmin)
