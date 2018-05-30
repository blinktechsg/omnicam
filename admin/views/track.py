from utility.models import Track
from project.models import Home
from blinktech.helpers.common import json_write_items
from django.views.generic import DetailView
from datetime import date
from django.http import HttpResponse
from django.utils import timezone

import json


def utility_track(request, pk):
    try:
        home = Home.get(pk)
        item = Track.objects.filter(home=home).order_by('-created')[:1]
    except Home.DoesNotExist:
        item = Track()
    except Track.DoesNotExist:
        item = Track()
    return json_write_items(item)


class TrackDetailView(DetailView):
    model = Track
    template_name = 'detail-view.html'


def home_track_chart(request, pk):
    today = date.today()
    try:
        home = Home.get(pk)
        items = Track.objects.filter(home=home).filter(created__contains=today).order_by('-created').values_list(
            'created',
            'bill_acc_cost', 'energy_main_acc_wh', 'power_main_w', 'energy_bg_acc_wh',
            'power_bg_w', 'voltage_v', 'current_a', 'peak_curr_acc_a'
        )[:50]
        items = reversed(items)
        chart = [["Bill", "Energy Main", "Power Main", "Energy BG", "Power BG",
                  "Voltage", "Current", "Peak Current"]]
        for item in items:
            t = timezone.localtime(item[0]).strftime('%H:%M')
            chart.append((
                t, item[1], item[2], item[3], item[4], item[5], item[6], item[7]
            ))
    except Home.DoesNotExist:
        chart = []
    except Track.DoesNotExist:
        chart = []

    return HttpResponse(json.dumps(chart), content_type='text/json')