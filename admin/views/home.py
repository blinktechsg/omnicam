from project.models import Home
from admin.forms import HomeForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView


class HomeListView(GenericListView):
    page = 'home'
    template_name = 'home-list.html'


class HomeCreateView(SuccessMessageMixin, CreateView):
    model = Home
    template_name = 'create-view.html'
    form_class = HomeForm
    success_message = 'Home Created'


class HomeDetailView(DetailView):
    model = Home
    template_name = 'home-detail.html'

    def get_context_data(self, **kwargs):
        data = super(HomeDetailView, self).get_context_data(**kwargs)
        home = data['object']
        if home and not home.slug:
            home.save()
            data['object'] = home
        return data


class CustomerHomeDetailView(DetailView):
    model = Home
    template_name = 'customer-home-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class HomeUpdateView(SuccessMessageMixin, UpdateView):
    model = Home
    template_name = 'update-view.html'
    form_class = HomeForm
    success_message = 'Home Updated Successfully'


class HomeDeleteView(SuccessMessageMixin, DeleteView):
    model = Home
    template_name = 'delete-view.html'
    success_message = 'Home Deleted'
