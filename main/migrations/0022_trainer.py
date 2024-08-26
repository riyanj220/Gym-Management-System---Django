# Generated by Django 5.0.2 on 2024-08-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_subscriber_subscriptiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(max_length=20)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='trainers')),
            ],
        ),
    ]