from django.urls import path
from . import views
from payment import webhooks as wh

urlpatterns = [
    path("process/", views.payment_process, name="process"),
    path("completed/", views.payment_completed, name="completed"),
    path("canceled/", views.payment_canceled, name="canceled"),
    path("webhook/", wh.stack_webhook, name="stack-webhook"),
]
