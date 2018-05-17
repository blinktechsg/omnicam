from django.db import models
from django.utils.translation import ugettext_lazy as _
from blinktech.db.models import BaseModel, NameValueModel


class Project(BaseModel):
    model_name = 'project'
    urlname_prefix = 'admin'
    fields = ['name', 'slug']

    name = models.CharField(_('project name'), max_length=64, null=True, blank=True)
    slug = models.SlugField(_('project slug'), null=True, blank=True)

    def __str__(self):
        return '%s' % self.name


class DeviceType(NameValueModel):
    model_name = 'devicetype'
    urlname_prefix = 'admin'
    fields = ['name', 'value', 'description']


class Home(NameValueModel):
    model_name = 'home'
    urlname_prefix = 'admin'
    fields = ['name', 'value', 'description', 'project']

    project = models.ForeignKey(Project)


class Hardware(NameValueModel):
    model_name = 'hardware'
    urlname_prefix = 'admin'

    fields = ['name', 'value', 'description', 'home']

    home = models.ForeignKey(Home)