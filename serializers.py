from rest_framework_gis import serializers

from .models import Border

class BorderSerializer(serializers.GeoFeatureModelSerializer):
    """Border full res GeoJSON serializer."""

    class Meta:
        fields = ("id", "name")
        geo_field = "geom"
        model = Border

class BorderLoSerializer(serializers.GeoFeatureModelSerializer):
    """Border lo res GeoJSON serializer."""

    class Meta:
        fields = ("id", "name")
        geo_field = "geom_lo"
        model = Border

class BorderMdSerializer(serializers.GeoFeatureModelSerializer):
    """Border md res GeoJSON serializer."""

    class Meta:
        fields = ("id", "name")
        geo_field = "geom_md"
        model = Border

class BorderHiSerializer(serializers.GeoFeatureModelSerializer):
    """Border hi res GeoJSON serializer."""

    class Meta:
        fields = ("id", "name")
        geo_field = "geom_hi"
        model = Border
