from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import HomeTextCard
from .models import AboutTextSection


# Class based views are extremely elegant


class HomeView(ListView):
    template_name = 'home.html'
    model = HomeTextCard
    queryset = HomeTextCard.objects.order_by('-date', '-id')


class HomeCardView(DetailView):
    template_name = 'card.html'
    model = HomeTextCard


class AboutView(ListView):
    template_name = 'about.html'
    model = AboutTextSection
