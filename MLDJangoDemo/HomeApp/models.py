from django.db import models
from django.utils.text import slugify
from datetime import date
from autoslug import AutoSlugField


class HomeTextCard(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=title, editable=True)
    date = models.DateField(default=date.today())
    body_short = models.CharField(max_length=250)
    body = models.TextField()
    url = models.URLField(max_length=250, blank=True)
    url_verbose = models.CharField(max_length=40, blank=True)
    internal_url = models.CharField(max_length=40, blank=True)
    internal_url_verbose = models.CharField(max_length=40, blank=True)


class AboutTextSection(models.Model):
    body = models.TextField()
