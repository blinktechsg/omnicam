from project.models import Project, Home, Hardware
from device.models import Device
from admin.forms import ProjectForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from admin.generic import GenericListView


class ProjectListView(GenericListView):
    page = 'project'


class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    template_name = 'create-view.html'
    form_class = ProjectForm
    success_message = 'Project Created'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'

    def get_context_data(self, **kwargs):
        data = super(ProjectDetailView, self).get_context_data(**kwargs)

        try:
            homes = Home.objects.filter(project=self.object)
            hm = []
            for home in homes:
                hardwares = Hardware.objects.filter(home=home)
                hw = []
                for hardware in hardwares:
                    devices = Device.objects.filter(hardware=hardware)
                    hw.append({'hardware': hardware, 'devices': devices})
                hm.append({'home': home, 'hardwares': hw})
        except Home.DoesNotExist:
            hm = None
        data['project'] = hm
        return data


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    template_name = 'update-view.html'
    form_class = ProjectForm
    success_message = 'Project Updated Successfully'


class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'delete-view.html'
    success_message = 'Project Deleted'
    success_url = reverse_lazy('admin:project:list')


