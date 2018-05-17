from device.models import Device, Status as DeviceStatus
from admin.forms import DeviceForm, DeviceStatusForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView


class DeviceListView(GenericListView):
    page = 'devices'


class DeviceCreateView(SuccessMessageMixin, CreateView):
    model = Device
    template_name = 'create-view.html'
    form_class = DeviceForm
    success_message = 'Device Created'


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'detail-view.html'


class DeviceUpdateView(SuccessMessageMixin, UpdateView):
    model = Device
    template_name = 'update-view.html'
    form_class = DeviceForm
    success_message = 'Device Updated Successfully'


class DeviceDeleteView(SuccessMessageMixin, DeleteView):
    model = Device
    template_name = 'delete-view.html'
    success_message = 'Device Deleted'


class DeviceStatusListView(GenericListView):
    page = 'devicestatus'


class DeviceStatusCreateView(SuccessMessageMixin, CreateView):
    model = DeviceStatus
    template_name = 'create-view.html'
    form_class = DeviceStatusForm
    success_message = 'DeviceStatus Created'


class DeviceStatusDetailView(DetailView):
    model = DeviceStatus
    template_name = 'detail-view.html'


class DeviceStatusUpdateView(SuccessMessageMixin, UpdateView):
    model = DeviceStatus
    template_name = 'update-view.html'
    form_class = DeviceStatusForm
    success_message = 'DeviceStatus Updated Successfully'


class DeviceStatusDeleteView(SuccessMessageMixin, DeleteView):
    model = DeviceStatus
    template_name = 'delete-view.html'
    success_message = 'DeviceStatus Deleted'

