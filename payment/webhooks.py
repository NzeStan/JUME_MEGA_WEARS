import hmac
import hashlib
import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .attatch_mail import payment_completed


if settings.DEBUG:
    secret = settings.PAYSTACK_TEST_SECRETE_KEY
else:
    secret = settings.PAYSTACK_LIVE_SECRETE_KEY


@csrf_exempt
def stack_webhook(request):
    print(request)
    # retrive the payload from the request body
    payload = request.body
    # signature header to to verify the request is from paystack
    sig_header = request.headers["x-paystack-signature"]
    body = None
    event = None

    try:
        # sign the payload with `HMAC SHA512`
        hash = hmac.new(
            secret.encode("utf-8"), payload, digestmod=hashlib.sha512
        ).hexdigest()
        # compare our signature with paystacks signature
        if hash == sig_header:
            # if signature matches,
            # proceed to retrive event status from payload
            body_unicode = payload.decode("utf-8")
            body = json.loads(body_unicode)
            # event status
            event = body["event"]
        else:
            raise Exception
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except KeyError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except:
        # Invalid signature
        return HttpResponse(status=400)

    if event == "charge.success":
        # if event status equals 'charge.success'
        # get the data and the `payment_id`
        # we'd set in the metadata ealier
        data, order_id = body["data"], body["data"]["metadata"]["order_id"]

        # validate status and gateway_response
        if (data["status"] == "success") and (data["gateway_response"] == "Successful"):
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # mark payment as paid
            order.paid = True
            order.save(force_update=True)

            print("PAID")

            payment_completed(order.id)

    return HttpResponse(status=200)
