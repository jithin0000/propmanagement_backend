from django.contrib.gis.db import models

# Create your models here.

class State(models.Model):
    country = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    enname = models.CharField(max_length=254)
    locname = models.CharField(max_length=254)
    offname = models.CharField(max_length=254)
    boundary = models.CharField(max_length=254)
    adminlevel = models.CharField(max_length=9)
    wikidata = models.CharField(max_length=254)
    wikimedia = models.CharField(max_length=254)
    timestamp = models.CharField(max_length=254)
    note = models.CharField(max_length=254)
    rpath = models.CharField(max_length=254)
    iso3166_2 = models.CharField(max_length=254)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name