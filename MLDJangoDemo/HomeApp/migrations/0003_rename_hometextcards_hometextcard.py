# Generated by Django 4.0.5 on 2022-07-03 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_alter_hometextcards_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeTextCards',
            new_name='HomeTextCard',
        ),
    ]
