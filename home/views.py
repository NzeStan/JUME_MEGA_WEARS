from django.views.generic import ListView, DetailView, DeleteView, View
from django.views.generic.edit import CreateView
from .models import Photo, Contact, Inspo, Video
from django.urls import reverse_lazy


class HomeCreateView(CreateView):
    model = Contact
    template_name = "home.html"
    fields = ["name", "email", "message"]
    success_url = reverse_lazy("home")


class Photos(ListView):
    model = Photo
    template_name = "photo.html"
    paginate_by = 4


class DetailPhotoView(DetailView):
    model = Photo
    template_name = "detail_photo.html"


class Inspos(ListView):
    model = Inspo
    template_name = "inspo.html"
    paginate_by = 4


class DetailInspoView(DetailView):
    model = Inspo
    template_name = "detail_inspo.html"


class Videos(ListView):
    model = Video
    template_name = "video.html"
    paginate_by = 4


class DetailVideoView(DetailView):
    model = Video
    template_name = "detail_video.html"


class NzeStan(ListView):
    model = Contact
    template_name = "nze.html"
    context_object_name = "contacts"


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contact_delete_view.html"
    success_url = reverse_lazy("nze_stan")
