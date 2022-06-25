from django.db import models
from django.utils.text import get_valid_filename
import os


def update_filename(instance, filename):

    # Originally made this to "fix" a problem with opencv imread, but the workaround was avoiding imread altogether
    # Kept because sanitizing the filename is still a good idea
    path = "images"
    name = get_valid_filename(filename)
    return os.path.join(path, name)


class CNNImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=update_filename)
    meme_confidence = models.FloatField(default=0)
    no_meme_confidence = models.FloatField(default=0)
    submitted_as_meme = models.BooleanField(default=False)
    was_processed = models.BooleanField(default=False)
    correct_prediction = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class CNN(models.Model):
    name = models.CharField(max_length=100)
    # No need to use but might do it in the future
