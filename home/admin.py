from django.contrib import admin
from .models import Contact, Photo, Inspo, Video


# Override the default site header
admin.site.site_header = "JUME MEGA WEARS & ACCESSORIES"


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
    )


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "video",
    )


class InspoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "inspo",
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "message",
    )


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Inspo, InspoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Contact, ContactAdmin)
