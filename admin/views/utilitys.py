from utility.models import Track, Daily, Monthly
from project.models import Home
from blinktech.helpers.common import json_write_items
from django.views.generic import DetailView


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
