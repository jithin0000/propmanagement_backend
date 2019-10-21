from django.contrib.gis.db import models

# Create your models here.
import uuid
from border.models import Border
from town.models import Town
from state.models import State

gender_choices = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other'),
    ('NOT', 'Prefer not to say')
]


def upload_to_agent_image(instance, filename):
    """ change image file name and upload """
    _,ext = filename.split('.')
    name = str(uuid.uuid4())
    return 'agent/{}/{}.{}'.format(instance.id, name, ext)



class Agent(models.Model):
    """ model for agent """

    name = models.CharField( max_length=155)
    gender = models.CharField(choices=gender_choices, max_length=150)
    birth_date = models.DateTimeField(auto_now_add=False)
    address1 = models.CharField( max_length=250, null=True, blank=True)
    address2 = models.CharField( max_length=250, null=True, blank=True)
    postal_code = models.CharField( max_length=250, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True)
    c_border = models.ForeignKey(Border, on_delete= models.PROTECT, null=True, blank=True)
    status = models.CharField(default="available", max_length=255)
    location = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CImages(models.Model):
    """ model for agent images """
    admin = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    default_pic = models.BooleanField(default=False)
    image_url = models.ImageField(upload_to=upload_to_agent_image)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url
