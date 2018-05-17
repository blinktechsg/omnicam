from project.models import Home
from admin.forms import HomeForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView


class HomeListView(GenericListView):
    page = 'home'


class HomeCreateView(SuccessMessageMixin, CreateView):
    model = Home
    template_name = 'create-view.html'
    form_class = HomeForm
    success_message = 'Home Created'


class HomeDetailView(DetailView):
    model = Home
    template_name = 'detail-view.html'


class HomeUpdateView(SuccessMessageMixin, UpdateView):
    model = Home
    template_name = 'update-view.html'
    form_class = HomeForm
    success_message = 'Home Updated Successfully'


class HomeDeleteView(SuccessMessageMixin, DeleteView):
    model = Home
    template_name = 'delete-view.html'
    success_message = 'Home Deleted'


