from device.models import Device, Status as DeviceStatus, Activity, Monthly
from admin.forms import DeviceForm, DeviceStatusForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from admin.generic import GenericListView
from blinktech.helpers.common import json_write_items
from datetime import date
from django.utils import timezone
import json


class DeviceListView(GenericListView):
    page = 'devices'
    template_name = 'device-list.html'


class DeviceCreateView(SuccessMessageMixin, CreateView):
    model = Device
    template_name = 'create-view.html'
    form_class = DeviceForm
    success_message = 'Device Created'


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'device-detail.html'

    def get_context_data(self, **kwargs):
        data = super(DeviceDetailView, self).get_context_data(**kwargs)
        try:
            status = DeviceStatus.objects.get(device=self.object)
        except DeviceStatus.DoesNotExist:
            status = DeviceStatus(device=self.object)

        data['status'] = status
        return data


class DeviceUpdateView(SuccessMessageMixin, UpdateView):
    model = Device
    template_name = 'update-view.html'
    form_class = DeviceForm
    success_message = 'Device Updated Successfully'


class DeviceDeleteView(SuccessMessageMixin, DeleteView):
    model = Device
    template_name = 'delete-view.html'
    success_message = 'Device Deleted'
    success_url = reverse_lazy('admin:devices:list')


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


def device_activity(request, pk):
    try:
        device = Device.get(pk)
        items = Activity.objects.filter(device=device).order_by('-created')[:20]
    except Device.DoesNotExist:
        items = Activity()
    except Activity.DoesNotExist:
        items = Activity()

    return json_write_items(items)


def device_monthly(request, pk):
    try:
        device = Device.get(pk)
        items = Monthly.objects.filter(device=device).order_by('-created')[:12]
    except Device.DoesNotExist:
        items = Monthly()
    except Monthly.DoesNotExist:
        items = Monthly()

    return json_write_items(items)


def device_activity_chart(request, pk):
    today = date.today()
    try:
        device = Device.get(pk)

        items = Activity.objects.filter(device=device).filter(created__contains=today).values_list('created', 'energy_wh', 'real_power_w')
        chart = [[device.name, 'Energy', 'Power']]
        if len(items) > 0:
            for item in items:
                t = timezone.localtime(item[0]).strftime('%H:%M')
                chart.append((t, item[1], item[2]))
        else:
            raise Device.DoesNotExist
    except Device.DoesNotExist:
        chart = [[device.name, 'Energy', 'Power'], ['', 0, 0]]

    return HttpResponse(json.dumps(chart), content_type="text/json")


