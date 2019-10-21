from django.contrib.gis import admin

# Register your models here.
from .models import Town

admin.site.register(Town, admin.OSMGeoAdmin)