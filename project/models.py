from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse_lazy
from blinktech.db.models import BaseModel, NameValueModel
from datetime import datetime
import hashlib


class Project(BaseModel):
    model_name = 'project'
    urlname_prefix = 'admin'
    fields = ['name', 'slug']

    name = models.CharField(_('project name'), max_length=64, null=True, blank=True)
    slug = models.SlugField(_('project slug'), null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def json(self):
        data = super(Project, self).json()
        data.update({'edit': self.update_url})
        data.update({'view': self.get_absolute_url()})
        data.update({'desc': self.slug})
        return data

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Project, self).save(*args, **kwargs)


class DeviceType(NameValueModel):
    model_name = 'devicetype'
    urlname_prefix = 'admin'
    fields = ['name']


class Home(NameValueModel):
    model_name = 'home'
    urlname_prefix = 'admin'
    slug = models.CharField(null=True, blank=True, max_length=20)
    project = models.ForeignKey(Project)

    fields = ['name', 'project']

    def json(self):
        data = super(Home, self).json()
        data.update({'customer': str(self.get_customer_url())})
        data.update({'edit': self.update_url})
        return data

    def get_customer_url(self):
        if self.slug:
            urlname = 'admin:home:customer'
            return reverse_lazy(urlname, kwargs={'slug': self.slug})
        else:
            return self.get_absolute_url()

    def save(self, *args, **kwargs):
        if not self.slug:
            m = hashlib.sha256()
            m.update(str(datetime.today()))
            self.slug = m.hexdigest()[:20]
        return super(Home, self).save(*args, **kwargs)


class Hardware(NameValueModel):
    model_name = 'hardware'
    urlname_prefix = 'admin'

    fields = ['name', 'home']

    home = models.ForeignKey(Home)