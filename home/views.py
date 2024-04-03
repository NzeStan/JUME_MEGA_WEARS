from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from .models import Photo, Contact, Inspo
from django.urls import reverse_lazy


class HomeCreateView(TemplateView):
    template_name = "home.html"


class Photos(ListView):
    model = Photo
    template_name = "photo.html"
    paginate_by = 20


class DetailPhotoView(DetailView):
    model = Photo
    template_name = "detail_photo.html"


class Inspos(ListView):
    model = Inspo
    template_name = "inspo.html"
    paginate_by = 20


class DetailInspoView(DetailView):
    model = Inspo
    template_name = "detail_inspo.html"


class NzeStan(ListView):
    model = Contact
    template_name = "nze.html"
    context_object_name = "contacts"


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contact_delete_view.html"
    success_url = reverse_lazy("nze_stan")


class AboutUsView(TemplateView):
    template_name = "about_us.html"


class ContactUsView(CreateView):
    model = Contact
    template_name = "contact_us.html"
    fields = ["name", "email", "message"]
    success_url = reverse_lazy("contact_us")
