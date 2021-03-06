# Generated by Django 4.0.5 on 2022-06-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemeDetector', '0005_remove_cnnimage_is_meme_cnnimage_meme_confidence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnnimage',
            name='submitted_as_meme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cnnimage',
            name='meme_confidence',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cnnimage',
            name='no_meme_confidence',
            field=models.FloatField(default=0),
        ),
    ]
