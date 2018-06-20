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
            'created', 'power_main_w'
        )
        count = len(items)
        items = reversed(items)
        chart = [["Time", "Energy Main"]]
        if count > 0:
            for item in items:
                t = timezone.localtime(item[0]).strftime('%H:%M')
                chart.append((
                    t, item[1]
                ))
        else:
            raise Track.DoesNotExist
    except Home.DoesNotExist:
        chart = [["Time", "Energy Main"], ["00:00", 0]]
    except Track.DoesNotExist:
        chart = [["Time", "Energy Main"], ["00:00", 0]]

    return HttpResponse(json.dumps(chart), content_type='text/json')