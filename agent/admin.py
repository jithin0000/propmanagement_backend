from django.contrib.gis import admin

# Register your models here.
from .models import Agent

admin.site.register(Agent, admin.OSMGeoAdmin)