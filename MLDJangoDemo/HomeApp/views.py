from django.views.generic.base import TemplateView

# Class based views are extremely elegant


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'
