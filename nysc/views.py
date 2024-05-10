from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Measurement, Event
from cart.forms import CartAddProductForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView
from django.utils import timezone
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductList(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm()
        if self.request.user.is_authenticated:
            user_measurement = Measurement.objects.filter(
                user=self.request.user
            ).first()
            context["user_measurement"] = user_measurement
        return context


class NyscLandingPage(TemplateView):
    template_name = "nysc_landing.html"
    model = Measurement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "measurement": self.model.objects.select_related("user").filter(
                user=self.request.user.id
            ),
        }
        return context


class CreateMeasurementView(LoginRequiredMixin, CreateView):
    model = Measurement
    fields = [
        "chest",
        "shoulder",
        "neck",
        "sleeve_length",
        "sleeve_round",
        "top_length",
        "waist",
        "thigh",
        "ankle",
        "laps",
        "knee",
        "trouser_length",
    ]
    success_url = reverse_lazy("product_list")
    template_name = "create_measurement.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(CreateMeasurementView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateMeasurementView, self).get_context_data(**kwargs)
        context["measurements"] = Measurement.objects.filter(user=self.request.user)
        return context


class UpdateMeasurementView(UpdateView):
    model = Measurement
    fields = [
        "chest",
        "shoulder",
        "neck",
        "sleeve_length",
        "sleeve_round",
        "top_length",
        "waist",
        "thigh",
        "ankle",
        "laps",
        "knee",
        "trouser_length",
    ]
    success_url = reverse_lazy("nysc_landing")
    template_name = "update_measurement.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(UpdateMeasurementView, self).form_valid(form)


"""
class EventDetailView(DetailView):
    model = Event
    template_name = "nysc_landing.html"
    context_object_name = "event"

    def get_object(self, queryset=None):
        return Event.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context["event_json"] = serialize("json", [event])
        context["current_datetime"] = timezone.now().isoformat()
        return context


def get_event_data(request):
    event = Event.objects.first()
    data = {
        "end_datetime": event.end_datetime.isoformat(),
    }
    return JsonResponse(data)

"""
