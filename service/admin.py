from django.contrib.gis import admin

# Register your models here.


from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.OSMGeoAdmin):
    '''Admin View for Service'''

    list_display = ('name','service_type')
    list_filter = ('name','service_type')
    search_fields = ('service_type','name')