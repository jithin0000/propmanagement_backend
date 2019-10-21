import os 
from django.contrib.gis.utils import LayerMapping

from .models import State


state_mapping = {
    'country': 'country',
    'name': 'name',
    'enname': 'enname',
    'locname': 'locname',
    'offname': 'offname',
    'boundary': 'boundary',
    'adminlevel': 'adminlevel',
    'wikidata': 'wikidata',
    'wikimedia': 'wikimedia',
    'timestamp': 'timestamp',
    'note': 'note',
    'rpath': 'rpath',
    'iso3166_2': 'ISO3166_2',
    'geom': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join('data/us', 'BoundarylineshapefileofUS14.shp'),
)

def run(verbose=True):
    lm = LayerMapping(State, world_shp, state_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
