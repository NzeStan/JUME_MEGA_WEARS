from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from .models import Product, Measurement
from cart.forms import CartAddProductForm
from django.views.generic.edit import UpdateView
from orders.models import Order
from django.urls import reverse_lazy


class ProductList(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_product_form"] = self.cart_product_form = CartAddProductForm()
        return context


class NyscLandingPage(TemplateView):
    template_name = "nysc_landing.html"
    model = Measurement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "measurement": self.model.objects.select_related(),
            "update_order": Order.objects.select_related(),
        }
        return context


class CreateMeasurementView(CreateView):
    model = Measurement
    fields = [
        "chest",
        "shoulder",
        "sleeve_length",
        "waist",
        "thigh",
        "trouser_length",
    ]
    success_url = reverse_lazy("nysc_landing")
    template_name = "create_measurement.html"


class UpdateMeasurementView(UpdateView):
    model = Measurement
    fields = [
        "chest",
        "shoulder",
        "sleeve_length",
        "waist",
        "thigh",
        "trouser_length",
    ]
    success_url = reverse_lazy("nysc_landing")
    template_name = "update_measurement.html"
