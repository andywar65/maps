from django.db import models
from django.utils.translation import gettext as _
from django.contrib.gis.db import models
from django.contrib.gis.geos import Polygon, MultiPolygon

class Border(models.Model):
    gid = models.BigIntegerField()
    gid2 = models.BigIntegerField()
    comune_bel = models.CharField(max_length=254)
    avdicm = models.CharField(max_length=254)
    classid = models.CharField(max_length=254)
    comune_ist = models.CharField(max_length=254)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)
    geom_lo = models.MultiPolygonField(srid=4326, null=True, blank=True)
    geom_md = models.MultiPolygonField(srid=4326, null=True, blank=True)
    geom_hi = models.MultiPolygonField(srid=4326, null=True, blank=True)

    def save(self, *args, **kwargs):
        a = self.geom.simplify(tolerance=0.01)
        b = self.geom.simplify(tolerance=0.001)
        c = self.geom.simplify(tolerance=0.0001)
        if a:
            if isinstance( a, ( Polygon, )):
                self.geom_lo = MultiPolygon(a)
                self.geom_md = MultiPolygon(b)
                self.geom_hi = MultiPolygon(c)
            elif isinstance( a, ( MultiPolygon, )):
                self.geom_lo = a
                self.geom_md = b
                self.geom_hi = c
        super(Border, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Border')
        verbose_name_plural = _('Borders')
        ordering = ('name', )
