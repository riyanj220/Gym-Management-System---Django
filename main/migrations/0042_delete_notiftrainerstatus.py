# Generated by Django 5.0.2 on 2024-09-18 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_trainernotification_is_read'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NotifTrainerStatus',
        ),
    ]
