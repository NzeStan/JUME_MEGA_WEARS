from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.models import Order


def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully paid.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f"JUME MEGA WEARS - Invoice no. {order.id}"
    message = "Please, find attached the invoice for your recent purchase."
    email = EmailMessage(subject, message, "jumemegawears@gmail.com", [order.email])
    # generate PDF
    html = render_to_string("pdf.html", {"order": order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    # attach PDF file
    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")
    # send e-mail
    email.send()
