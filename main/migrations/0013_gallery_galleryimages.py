# Generated by Django 5.0.2 on 2024-08-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_enquiry_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField(max_length=150)),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='gallery_imgs')),
            ],
        ),
    ]
