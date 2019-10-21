
from django.contrib.gis.utils import LayerMapping
import os

from .models import Town

town_mapping = {
    'objectid': 'objectid',
    'tcity15cd': 'tcity15cd',
    'tcity15nm': 'tcity15nm',
    'st_areasha': 'st_areasha',
    'st_lengths': 'st_lengths',
    'geom': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join('data/uk', 'Major_Towns_and_Cities_December_2015_Boundaries.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Town, world_shp, town_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
