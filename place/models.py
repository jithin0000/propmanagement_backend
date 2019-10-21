from django.contrib.gis.db import models

# Create your models here.


class Country(models.Model):
    """ model for country """
    name = models.CharField(max_length=255)
    border = models.PolygonField()

    created_at = models.DateTimeField(  auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    """ model for city """
    name = models.CharField(max_length=255)
    city_border = models.PolygonField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    created_at = models.DateTimeField(  auto_now_add=True)


    def __str__(self):
        return self.name
    

