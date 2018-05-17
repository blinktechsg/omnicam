from project.models import DeviceType
from admin.forms import DeviceTypeForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView


class DeviceTypeListView(GenericListView):
    page = 'devicetype'


class DeviceTypeCreateView(SuccessMessageMixin, CreateView):
    model = DeviceType
    template_name = 'create-view.html'
    form_class = DeviceTypeForm
    success_message = 'Device Type Created'


class DeviceTypeDetailView(DetailView):
    model = DeviceType
    template_name = 'detail-view.html'


class DeviceTypeUpdateView(SuccessMessageMixin, UpdateView):
    model = DeviceType
    template_name = 'update-view.html'
    form_class = DeviceTypeForm
    success_message = 'Device Type Updated Successfully'


class DeviceTypeDeleteView(SuccessMessageMixin, DeleteView):
    model = DeviceType
    template_name = 'delete-view.html'
    success_message = 'Device Type Deleted'


