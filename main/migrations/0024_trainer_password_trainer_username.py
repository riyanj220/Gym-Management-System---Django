# Generated by Django 5.0.2 on 2024-08-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_trainer_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]