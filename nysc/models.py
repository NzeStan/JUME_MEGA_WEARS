from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Product(models.Model):
    TYPE_CHOICES = [
        ("kakhi", "kakhi"),
        ("vest", "vest"),
        ("cap", "cap"),
        # Add more choices as needed
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="jume_nysc_products", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, default="M", blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nysc_detail", args=[str(self.id)])

    class Meta:
        ordering = ["id"]


class Measurement(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    chest = models.IntegerField(null=True)
    shoulder = models.IntegerField(null=True)
    neck = models.IntegerField(null=True)
    sleeve_length = models.IntegerField(null=True)
    sleeve_round = models.IntegerField(null=True)
    top_length = models.IntegerField(null=True)
    waist = models.IntegerField(null=True)
    thigh = models.IntegerField(null=True)
    ankle = models.IntegerField(null=True)
    laps = models.IntegerField(null=True)
    knee = models.IntegerField(null=True)
    trouser_length = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("update_measurement", args=[str(self.id)])
