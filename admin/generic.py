from django.views.generic import TemplateView
from django.urls import reverse_lazy

from blinktech.helpers.common import json_write_items
from project.models import Project, DeviceType, Home
from device.models import (Device, Status as DeviceStatus,
                           Activity as DeviceActivity, Monthly as DeviceMonthy)
from utility.models import (Track as UtilityTrack, Daily as UtilityDaily, Monthly as UtilityMonthly)


class GenericListView(TemplateView):
    page = ''
    template_name = 'list-view.html'

    def get_context_data(self, **kwargs):
        data = super(GenericListView, self).get_context_data(**kwargs)
        data['list'] = reverse_lazy('admin:json-list', kwargs={'page': self.page})
        data['page'] = self.page

        return data


def json_view(request, page):
    model_list = {Project.model_name: Project, DeviceStatus.model_name: DeviceStatus,
                  Device.model_name: Device, DeviceType.model_name: DeviceType,
                  DeviceActivity.model_name: DeviceActivity, DeviceMonthy.model_name: DeviceMonthy,
                  UtilityTrack.model_name: UtilityTrack, UtilityDaily.model_name: UtilityDaily,
                  Home.model_name: Home, UtilityMonthly.model_name: UtilityMonthly,
                  }

    try:
        model = model_list[page]
        items = model.objects.all()
        return json_write_items(items)
    except LookupError:
        raise
