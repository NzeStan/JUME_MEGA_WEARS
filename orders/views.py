from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            request.session["order_id"] = order.id
            # redirect for payment
            return redirect(reverse("process"))

    else:
        form = OrderCreateForm()
    return render(request, "create.html", {"cart": cart, "form": form})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


class UpdateOrderView(UpdateView):
    model = Order
    fields = ["state_of_deployment", "nysc_call_up_number"]
    success_url = reverse_lazy("nysc_landing")
    template_name = "update_order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "order_update": self.model.objects.select_related("user"),
        }
        return context


@staff_member_required
def state_aba(request):
    order = OrderItem.objects.select_related("order", "product")
    html = render_to_string("state_aba.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_Aba.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response
