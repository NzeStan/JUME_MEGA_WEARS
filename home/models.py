from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="jume_images/", blank=True)

    def get_absolute_url(self):
        return reverse("detail_photo", args=[str(self.id)])


class Inspo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspo = models.ImageField(upload_to="jume_inspos/", blank=True)

    def get_absolute_url(self):
        return reverse("detail_inspo", args=[str(self.id)])


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
