from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from maps.models import Border

# Auto-generated `LayerMapping` dictionary for Border model
border_mapping = {
    'gid': 'gid',
    'gid2': '__gid',
    'comune_bel': 'comune_bel',
    'avdicm': 'avdicm',
    'classid': 'classid',
    'comune_ist': 'comune_ist',
    'name': 'comune_com',
    'geom': 'MULTIPOLYGON',
}

shapes = Path(__file__).resolve().parent / 'prova_qgis' / 'comuni.shp'

def run(verbose=True):
    lm = LayerMapping(Border, shapes, border_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)
