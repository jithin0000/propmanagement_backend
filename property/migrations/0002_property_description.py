# Generated by Django 2.2 on 2019-10-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
