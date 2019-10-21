from django.contrib.gis.db import models

# Create your models here.
from place.models import Country, City
from border.models import Border
from town.models import Town

service_choices = [
    ('PARK','Park'),
    ('HEALTH_CARE','Health Care'),
    ('HEALTH_CLUB','Health Club'),
    ('RESTAURANT','Restuarant'),
    ('SCHOOL','School'),
    ('FOODSTORE','Food Store'),
]
import uuid

def upload_to_service(instance, filename):
    """ changing name of file """
    _,ext = filename.split('.')
    name = str(uuid.uui4())
    return 'service/{}/{}.{}'.format(instance.name, name,ext)

class Service(models.Model):
    """ model for near by school """

    name = models.CharField(unique=True, max_length=155)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to=upload_to_service, null=True, blank=True)


    address = models.CharField( max_length=150)
    address2 = models.CharField( max_length=150)
    region = models.ForeignKey(Town, on_delete=models.PROTECT, null=True, blank=True)
    c_border = models.ForeignKey(Border, on_delete= models.PROTECT, null=True, blank=True)

    service_type = models.CharField(choices=service_choices, max_length=255)
    postal_code = models.CharField( max_length=155)
    contact = models.BigIntegerField(default=0)

    location = models.PointField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



