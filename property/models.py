from django.contrib.gis.db import models

# Create your models here.
import uuid
from border.models import Border
from town.models import Town
from agent.models import Agent
from state.models import State

sale_choices = [
    ('SALE', "Sale"),
    ('RENT', "Rent")
]

prop_choices = [
    ('HOUSE', "House"),
    ('FLAT', "Flat"),
    ('OTHER', "Other")
]

class Property(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField( max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    prop_type = models.CharField( choices=prop_choices, max_length=150)
    room = models.IntegerField(default=0, null=True, blank=True)
    bath_rooms = models.IntegerField(default=0, null=True, blank=True)
    bed_room = models.IntegerField(default=0)
    square_meter = models.FloatField(default=0.0, null=True, blank=True)
    sale_type = models.CharField(choices=sale_choices, max_length=150)
    address1 = models.CharField( max_length=250, null=True, blank=True)
    address2 = models.CharField( max_length=250, null=True, blank=True)
    postal_code = models.CharField( max_length=250, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True)
    c_border = models.ForeignKey(Border, on_delete= models.PROTECT, null=True, blank=True)
    status = models.CharField(default="available", max_length=255)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "properties"


    def __str__(self):
        return self.name


def upload_with_rename(instance, filename):
    name = str(uuid.uuid4())
    _,extension = filename.split('.')
    return "{}/{}.{}".format(instance.id,name,extension)




class PropImage(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    prop_image_url = models.ImageField(upload_to=upload_with_rename, max_length=None)

    def __str__(self):
        return str(self.id)