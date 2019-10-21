from django.contrib.gis import admin

# Register your models here.
from property.models import Property,PropImage

@admin.register(Property)
class PropertyAdmin(admin.OSMGeoAdmin):
    '''Admin View for Property'''

    list_display = ('name','price', 'location')
    list_filter = ('name','price')
    search_fields = ('name','city')
    


admin.site.register(PropImage)
