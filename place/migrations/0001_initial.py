# Generated by Django 2.2 on 2019-10-18 09:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('border', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city_border', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Country')),
            ],
        ),
    ]