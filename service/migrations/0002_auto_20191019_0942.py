# Generated by Django 2.2 on 2019-10-19 04:12

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=service.models.upload_to_service),
        ),
    ]
