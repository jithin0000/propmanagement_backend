from django.contrib.gis import admin

# Register your models here.
from .models import Country, City


admin.site.register(Country, admin.OSMGeoAdmin)
admin.site.register(City, admin.OSMGeoAdmin)