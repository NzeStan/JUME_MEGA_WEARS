from django.db import models
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.urls import reverse


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="jume_images/", blank=True)

    def get_absolute_url(self):
        return reverse("detail_photo", args=[str(self.id)])


class Inspo(models.Model):
    inspo = models.ImageField(upload_to="jume_inspos/", blank=True)

    def get_absolute_url(self):
        return reverse("detail_inspo", args=[str(self.id)])


class Video(models.Model):
    video = models.FileField(
        upload_to="jume_videos/",
        blank=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video],
    )

    def get_absolute_url(self):
        return reverse("detail_video", args=[str(self.id)])


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
