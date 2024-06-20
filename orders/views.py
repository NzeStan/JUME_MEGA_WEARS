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
from django.db.models import Count, Sum
from payment.attatch_mail import payment_completed
import logging
from django.contrib import messages
from django.db import transaction
# Create your views here.

logger = logging.getLogger(__name__)

@login_required
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save()
                    current_user = request.user
                    try:
                        measurement = Measurement.objects.get(user=current_user)
                    except Measurement.DoesNotExist:
                        logger.warning(f"Measurement not found for user {current_user.id}")
                        measurement = None

                    for item in cart:
                        order_item_data = {
                            "order": order,
                            "product": item["product"],
                            "price": item["price"],
                            "quantity": item["quantity"],
                            "user": current_user,
                        }
                        if measurement:
                            order_item_data["measurement_id"] = measurement.id

                        OrderItem.objects.create(**order_item_data)

                    cart.clear()
                    payment_completed(order.id)
                    request.session["order_id"] = order.id

                return redirect(reverse("process"))
            except Exception as e:
                logger.error(f"Error creating order: {str(e)}")
                messages.error(request, "An error occurred while processing your order. Please try again.")
        else:
            messages.error(request, "Please correct the errors in the form.")
    
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
def state_abuja(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Abuja")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Abuja")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Abuja.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Abuja.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_abia(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Abia")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Abia")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Abia.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Abia.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_adamawa(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Adamawa")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Adamawa")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Adamawa.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Adamawa.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_akwa_ibom(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Akwa Ibom")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Akwa Ibom")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Akwa_Ibom.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Akwa Ibom.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_anambra(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Anambra")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Anambra")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Anambra.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Anambra.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_bauchi(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Bauchi")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Bauchi")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Bauchi.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Bauchi.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_bayelsa(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Bayelsa")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Bayelsa")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Bayelsa.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Bayelsa.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_benue(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Benue")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Benue")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Benue.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Benue.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_borno(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Borno")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Borno")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Borno.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Borno.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_cross_river(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Cross River")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Cross River")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Cross_River.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Cross River.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_delta(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Delta")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Delta")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Delta.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Delta.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_ebonyi(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Ebonyi")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Ebonyi")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Ebonyi.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Ebonyi.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_edo(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Edo")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Edo")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Edo.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Edo.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_ekiti(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Ekiti")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Ekiti")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Ekiti.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Ekiti.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_enugu(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Enugu")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Enugu")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_enugu.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Enugu.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_gombe(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Gombe")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Gombe")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Gombe.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Gombe.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_imo(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Imo")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Imo")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_imo.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Imo.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_jigawa(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Jigawa")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Jigawa")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Jigawa.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Jigawa.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_kaduna(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Kaduna")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Kaduna")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Kaduna.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Kaduna.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_kano(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Kano")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Kano")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Kano.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Kano.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_katsina(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Katsina")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Katsina")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Katsina.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Katsina.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_kebbi(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Kebbi")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Kebbi")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Kebbi.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Kebbi.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_kogi(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Kogi")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Kogi")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Kogi.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Kogi.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_kwara(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Kwara")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Kwara")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Kwara.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Kwara.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_lagos(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Lagos")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Lagos")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Lagos.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Lagos.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_nassarawa(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Nassarawa")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Nassarawa")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Nassarawa.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Nassarawa.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_niger(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Niger")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Niger")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Niger.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Niger.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_ogun(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Ogun")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Ogun")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Ogun.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Ogun.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_ondo(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Ondo")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Ondo")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Ondo.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Ondo.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_osun(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Osun")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Osun")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Osun.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Osun.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_oyo(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Oyo")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Oyo")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Oyo.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Oyo.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_plateau(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Plateau")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Plateau")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Plateau.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Plateau.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_rivers(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Rivers")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Rivers")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Rivers.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Rivers.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_sokoto(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Sokoto")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Sokoto")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Sokoto.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Sokoto.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_taraba(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Taraba")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Taraba")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Taraba.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Taraba.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_yobe(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Yobe")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Yobe")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Yobe.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Yobe.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def state_zamfara(request):
    order_items = OrderItem.objects.select_related(
        "order", "product", "user", "measurement"
    ).filter(order__paid=True, user__state_of_deployment="Zamfara")
    summary_query = (
        OrderItem.objects.values("product__name", "product__size")
        .annotate(
            total_count=Count("id"),
            total_sum=Sum("quantity"),
        )
        .filter(order__paid=True, user__state_of_deployment="Zamfara")
    )
    context = {
        "order_items": order_items,
        "user": request.user,
        "summary_query": summary_query,
    }
    html = render_to_string("state_Zamfara.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=Order_Zamfara.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response
