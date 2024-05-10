from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
import json
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from orders.models import Order
from decimal import Decimal

# create the Paystack instance
if settings.DEBUG:
    api_key = settings.PAYSTACK_TEST_SECRETE_KEY
else:
    api_key = settings.PAYSTACK_LIVE_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL


def payment_process(request):
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(Order, id=order_id)
    amount = order.get_total_cost()

    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("completed"))
        cancel_url = request.build_absolute_uri(reverse("canceled"))

        # metadata to pass additional data that
        # the endpoint doesn't accept naturally.
        metadata = json.dumps(
            {
                "order_id": order_id,
                "cancel_action": cancel_url,
            }
        )

        # Paystack checkout session data
        session_data = {
            "email": order.email,
            "amount": int(amount) * 100,
            "callback_url": success_url,
            "metadata": metadata,
        }
        headers = {"authorization": f"Bearer {api_key}"}
        # API request to paystack server
        r = requests.post(url, headers=headers, data=session_data)
        response = r.json()
        if response["status"] == True:
            # redirect to Paystack payment form
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass
        else:
            return render(request, "process.html", locals())
    else:
        return render(request, "process.html", locals())


def payment_completed(request):
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(Order, id=order_id)

    # retrive the query parameter from the request object
    ref = request.GET.get("reference", "")  # new
    # verify transaction endpoint
    url = "https://api.paystack.co/transaction/verify/{}".format(ref)  # new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}  # new
    r = requests.get(url, headers=headers)  # new
    res = r.json()  # new
    res = res["data"]

    # verify status before setting payment_ref
    if res["status"] == "success":  # new
        # update payment payment reference
        order.paystack_ref = ref  # new
        order.save()  # new

    return render(request, "completed.html")


def payment_canceled(request):
    return render(request, "canceled.html")
