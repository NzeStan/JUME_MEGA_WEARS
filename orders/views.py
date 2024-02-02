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
from django.contrib.auth import get_user_model
from nysc.models import Measurement

# Create your views here.


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            current_user = request.user
            measurement = Measurement.objects.get(user=current_user)

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                    measurement_id=measurement.id,
                    user=current_user,
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


@staff_member_required
def state_aba(request):
    order_items = OrderItem.objects.select_related("order", "product", "user")
    context = {"order_items": order_items, "user": request.user}
    html = render_to_string("state_aba.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_Aba.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response