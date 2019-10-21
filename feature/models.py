from django.db import models

# Create your models here.
from property.models import Property

class Feature(models.Model):
    """ main features of Property """
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=255)
    description = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feature_name