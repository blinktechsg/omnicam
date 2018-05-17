from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from blinktech.db.models import BaseModel
from project.models import Project, Home, DeviceType, Hardware


class Device(BaseModel):
    model_name = 'devices'
    urlname_prefix = 'admin'

    name = models.CharField(_('device name'), max_length=64)
    type = models.ForeignKey(DeviceType)

    hardware = models.ForeignKey(Hardware)

    fields = ['name', 'type', 'hardware']

    def __str__(self):
        return '%s' % self.name


class DeviceBase(BaseModel):
    fields = ['device', 'on_time', 'off_time', 'real_power_w', 'energy_wh']

    device = models.ForeignKey(Device)
    on_time = models.DateTimeField(_('on date time'), null=False)
    off_time = models.DateTimeField(_('off date time'), null=True)
    real_power_w = models.IntegerField(_('real power in w'), default=0)
    energy_wh = models.IntegerField(_('energy in wh'), default=0)

    class Meta:
        abstract = True


class Status(DeviceBase):
    model_name = 'devicestatus'
    urlname_prefix = 'admin'


class Activity(DeviceBase):
    model_name = 'activity'
    urlname_prefix = 'admin'

    @classmethod
    def get_latest(cls, last_id=1):
        try:
            items = cls.objects.order_by('-id')[:10]
            return items
        except cls.DoesNotExist:
            raise

    def get_absolute_url(self):
        return ''

    def json(self):
        data = super(Activity, self).json()
        data['on_time'] = timezone.localtime(self.on_time).strftime('%d %b %Y %I:%M:%S %p')
        data['off_time'] = timezone.localtime(self.off_time).strftime('%d %b %Y %I:%M:%S %p')

        return data


class Monthly(DeviceBase):
    model_name = 'devicemonthly'
    urlname_prefix = 'admin'

