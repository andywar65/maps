from rest_framework import generics
from rest_framework_gis import filters

from .models import Border
from .serializers import *

class BordersApiView(generics.ListAPIView):

    bbox_filter_field = "geom"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    bbox_filter_include_overlapping = True

class BordersApiLoView(generics.ListAPIView):

    bbox_filter_field = "geom_lo"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Border.objects.all()
    serializer_class = BorderLoSerializer
    bbox_filter_include_overlapping = True

class BordersApiMdView(generics.ListAPIView):

    bbox_filter_field = "geom_md"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Border.objects.all()
    serializer_class = BorderMdSerializer
    bbox_filter_include_overlapping = True

class BordersApiHiView(generics.ListAPIView):

    bbox_filter_field = "geom_hi"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Border.objects.all()
    serializer_class = BorderHiSerializer
    bbox_filter_include_overlapping = True
