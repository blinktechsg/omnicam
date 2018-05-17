from device.models import Activity
from blinktech.helpers.common import json_write_items


def get_activity(request):
    try:
        last = request.GET['last']
    except KeyError:
        last = 1

    items = Activity.get_latest(last_id=last)
    return json_write_items(items)


