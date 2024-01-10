from django.views.generic import ListView, DetailView, TemplateView
from .models import Product
from cart.forms import CartAddProductForm


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
