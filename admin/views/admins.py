from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from project.models import Home
from utility.models import Track


@method_decorator(ensure_csrf_cookie, 'dispatch')
class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        try:
            home_id = request.GET['home']
            home = Home.get(home_id)
            request.session['home'] = home.id
            messages.add_message(request, messages.INFO, message='Now viewing Home %s' % str(home))
            try:
                utility = Track.objects.get(home=home)
            except Track.DoesNotExist:
                utility = Track(home=home)
            return render(request, self.template_name, {'home': home, 'utility': utility})
        except KeyError:
            homes = Home.objects.all()

            return render(request, 'homes-index.html', {'homes': homes})


@method_decorator(ensure_csrf_cookie, 'dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        data = super(Dashboard, self).get_context_data(**kwargs)

        return data

    def get(self, request, *args, **kwargs):
        try:
            home = Home.get(request.session['home'])
        except KeyError:
            return reverse_lazy('index')


class HomeActivity(TemplateView):
    template_name = 'home-activity.html'

    def get(self, request, *args, **kwargs):
        try:
            home = Home.get(request.session['home'])
        except KeyError:
            return reverse_lazy('index')