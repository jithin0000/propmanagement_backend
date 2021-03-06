# Generated by Django 2.2 on 2019-10-19 03:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0002_auto_20191018_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=150)),
                ('service_type', models.CharField(choices=[('PARK', 'Park'), ('HEALTH_CARE', 'Health Care'), ('HEALTH_CLUB', 'Health Club'), ('RESTAURANT', 'Restuarant'), ('SCHOOL', 'School'), ('FOODSTORE', 'Food Store')], max_length=255)),
                ('region', models.CharField(max_length=155)),
                ('postal_code', models.CharField(max_length=155)),
                ('contact', models.BigIntegerField(default=0)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.Country')),
            ],
        ),
    ]
