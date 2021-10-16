from django.views.generic.base import TemplateView

class BordersMapView(TemplateView):
    """Borders map view."""

    template_name = "maps/border_map.html"
