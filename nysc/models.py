from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="jume_nysc_products", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, default="M", blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nysc_detail", args=[str(self.id)])


class Measurement(models.Model):
    chest = models.IntegerField()
    shoulder = models.IntegerField()
    sleeve_length = models.IntegerField()
    waist = models.IntegerField()
    thigh = models.IntegerField()
    trouser_length = models.IntegerField()

    def get_absolute_url(self):
        return reverse("update_measurement", args=[str(self.id)])

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
