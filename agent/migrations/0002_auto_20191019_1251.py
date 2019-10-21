# Generated by Django 2.2 on 2019-10-19 07:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('border', '0002_auto_20191019_1147'),
        ('town', '0001_initial'),
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='address1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='address2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='c_border',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='border.Border'),
        ),
        migrations.AddField(
            model_name='agent',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='agent',
            name='postal_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='town.Town'),
        ),
        migrations.AddField(
            model_name='agent',
            name='status',
            field=models.CharField(default='available', max_length=255),
        ),
    ]
