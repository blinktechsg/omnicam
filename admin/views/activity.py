from device.models import Activity, Device, Status
from project.models import Home, Hardware
from blinktech.helpers.common import json_write_items


def get_activity(request):
    try:
        last = request.GET['last']
    except KeyError:
        last = 1

    items = Activity.get_latest(last_id=last)
    return json_write_items(items)


def get_home_devices(request):
    try:
        home = Home.get(request.GET['home'])
        hardwares = Hardware.objects.filter(home=home)
        devices = Device.objects.filter(hardware=hardwares)
    except KeyError:
        devices = None

    items = []
    for device in devices:
        try:
            status = Status.objects.get(device=device)
            items.append(status)
        except Status.DoesNotExist:
            continue

    return json_write_items(items)

