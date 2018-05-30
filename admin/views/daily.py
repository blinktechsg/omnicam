from utility.models import Daily
from project.models import Home
from blinktech.helpers.common import json_write_items
from django.views.generic import DetailView


def utility_daily(request, pk):
    try:
        home = Home.get(pk)
        item = Daily.objects.filter(home=home).order_by('-created')[:30]
    except Home.DoesNotExist:
        item = Daily()
    except Daily.DoesNotExist:
        item = Daily()

    return json_write_items(item)


class DailyDetailView(DetailView):
    model = Daily
    template_name = 'detail-view.html'
