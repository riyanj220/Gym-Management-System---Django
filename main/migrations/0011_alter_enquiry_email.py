# Generated by Django 5.0.2 on 2024-08-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.TextField(max_length=20),
        ),
    ]