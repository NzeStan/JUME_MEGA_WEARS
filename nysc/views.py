from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Measurement
from cart.forms import CartAddProductForm
from orders.models import Order
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.urls import reverse


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
            "measurement": self.model.objects.select_related("user").filter(
                user=self.request.user.is_authenticated
            ),
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
        "sleeve_length",
        "waist",
        "thigh",
        "trouser_length",
    ]
    success_url = reverse_lazy("nysc_landing")
    template_name = "update_measurement.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(UpdateMeasurementView, self).form_valid(form)
