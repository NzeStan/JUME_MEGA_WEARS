from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class Update_User_Detail(UpdateView):
    model = get_user_model()
    fields = [
        "nysc_call_up_number",
        "state_of_deployment",
        "phone_number",
    ]
    success_url = reverse_lazy("nysc_landing")
    template_name = "update_user_detail.html"
