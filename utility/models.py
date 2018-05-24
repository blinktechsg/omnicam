from django.db import models
from django.utils.translation import ugettext_lazy as _
from blinktech.db.models import BaseModel
from project.models import Home

from datetime import datetime


class UtilityBase(BaseModel):
    fields = ['home', 'bill_acc_cost', 'energy_main_acc_wh', 'power_main_w',
              'energy_bg_acc_wh', 'power_bg_w', 'voltage_v', 'current_a', 'peak_curr_acc_a',
              'datetime_peak_acc']
    home = models.ForeignKey(Home)
    bill_acc_cost = models.FloatField(_('bill accumulated cost'), default=0.0)
    energy_main_acc_wh = models.IntegerField(_('energy main accumulated in wh'), default=0)
    power_main_w = models.IntegerField(_('power main in w'), default=0)
    energy_bg_acc_wh = models.FloatField(_('energy background accumulated in wh'), default=0, null=False)
    power_bg_w = models.FloatField(_('power background in w'), default=0, null=False)
    voltage_v = models.FloatField(_('voltage in v'), default=0.0)
    current_a = models.FloatField(_('current in a'), default=0.0)
    peak_curr_acc_a = models.FloatField(_('peak current in a'), default=0.0)
    datetime_peak_acc = models.DateTimeField()

    class Meta:
        abstract = True


class Track(UtilityBase):
    model_name = 'utilitytrack'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_track_home')

    @classmethod
    def get_today(cls):
        try:
            item = cls.objects.filter(created=datetime.today())
            return item
        except cls.DoesNotExist:
            raise


class Daily(UtilityBase):
    model_name = 'utilitydaily'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_daily_home')


class Monthly(UtilityBase):
    model_name = 'utilitymonthly'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_monthly_home')

