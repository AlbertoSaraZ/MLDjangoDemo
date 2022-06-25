from django.apps import AppConfig
from django.db.models.signals import post_save


class MemedetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MemeDetector'

    def ready(self):
        from . import signals, models
        post_save.connect(signals.process_new_image, sender=models.CNNImage)
