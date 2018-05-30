from django.db import models
from django.utils import timezone
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

    def get_day(self):
        return timezone.localtime(self.updated).strftime('%d-%b')

    def get_month(self):
        return timezone.localtime(self.updated).strftime('%b %Y')

    def json(self):
        data = super(UtilityBase, self).json()

        data.update({'today': self.get_day()})
        data.update({'this_month': self.get_month()})

        return data


class Track(UtilityBase):
    model_name = 'track'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_track_home')

    @classmethod
    def get_today(cls):
        try:
            item = cls.objects.filter(created__date=datetime.today())
            return item
        except cls.DoesNotExist:
            raise

    @classmethod
    def get_today_by_home(cls, home):
        try:
            item = cls.objects.filter(created__date=datetime.today()).filter(home=home)
            return item
        except cls.DoesNotExist:
            raise


class Daily(UtilityBase):
    model_name = 'daily'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_daily_home')


class Monthly(UtilityBase):
    model_name = 'monthly'
    urlname_prefix = 'admin'

    home = models.ForeignKey(Home, related_name='utility_monthly_home')

