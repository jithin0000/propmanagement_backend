# Generated by Django 2.2 on 2019-10-20 11:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('enname', models.CharField(max_length=254)),
                ('locname', models.CharField(max_length=254)),
                ('offname', models.CharField(max_length=254)),
                ('boundary', models.CharField(max_length=254)),
                ('adminlevel', models.CharField(max_length=9)),
                ('wikidata', models.CharField(max_length=254)),
                ('wikimedia', models.CharField(max_length=254)),
                ('timestamp', models.CharField(max_length=254)),
                ('note', models.CharField(max_length=254)),
                ('rpath', models.CharField(max_length=254)),
                ('iso3166_2', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]