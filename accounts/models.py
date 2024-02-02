from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    nysc_call_up_number = models.CharField(max_length=150, blank=True)
    state_of_deployment = models.CharField(max_length=150, blank=True)
