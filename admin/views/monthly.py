from utility.models import Monthly
from project.models import Home
from blinktech.helpers.common import json_write_items
from django.views.generic import DetailView


def utility_monthly(request, pk):
    try:
        home = Home.get(pk)
        item = Monthly.objects.filter(home=home).order_by('-created')[:12]
    except Home.DoesNotExist:
        item = Monthly()
    except Monthly.DoesNotExist:
        item = Monthly()

    return json_write_items(item)


class MonthlyDetailView(DetailView):
    model = Monthly
    template_name = 'detail-view.html'
