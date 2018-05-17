from project.models import Project
from admin.forms import ProjectForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
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
    template_name = 'detail-view.html'


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    template_name = 'update-view.html'
    form_class = ProjectForm
    success_message = 'Project Updated Successfully'


class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'delete-view.html'
    success_message = 'Project Deleted'


