# Generated by Django 2.2 on 2019-10-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_auto_20191020_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='birth_date',
            field=models.DateField(),
        ),
    ]