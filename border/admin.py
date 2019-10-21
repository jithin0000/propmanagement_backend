from django.contrib.gis import admin

# Register your models here.

from .models import Border

admin.site.register(Border, admin.OSMGeoAdmin)
