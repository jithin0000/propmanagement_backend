from django.contrib.gis.db import models

# Create your models here.

class Town(models.Model):
    objectid = models.BigIntegerField()
    tcity15cd = models.CharField(max_length=80)
    tcity15nm = models.CharField(max_length=80)
    st_areasha = models.FloatField()                                                                                        
    st_lengths = models.FloatField()                                                                                        
    geom = models.MultiPolygonField()    

    def __str__(self):
        return self.tcity15nm