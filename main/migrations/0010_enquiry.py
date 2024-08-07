# Generated by Django 5.0.2 on 2024-08-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('query', models.TextField(max_length=100)),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
