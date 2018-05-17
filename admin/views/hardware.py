from project.models import Hardware
from admin.forms import HardwareForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView


class HardwareListView(GenericListView):
    page = 'hardware'


class HardwareCreateView(SuccessMessageMixin, CreateView):
    model = Hardware
    template_name = 'create-view.html'
    form_class = HardwareForm
    success_message = 'Hardware Created'


class HardwareDetailView(DetailView):
    model = Hardware
    template_name = 'detail-view.html'


class HardwareUpdateView(SuccessMessageMixin, UpdateView):
    model = Hardware
    template_name = 'update-view.html'
    form_class = HardwareForm
    success_message = 'Hardware Updated Successfully'


class HardwareDeleteView(SuccessMessageMixin, DeleteView):
    model = Hardware
    template_name = 'delete-view.html'
    success_message = 'Hardware Deleted'


