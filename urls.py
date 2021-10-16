from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from .views import *
from .api_views import *

app_name = 'maps'
urlpatterns = [
    path('', BordersMapView.as_view(), name = 'borders'),
    path('api/borders/lo/', BordersApiLoView.as_view(), ),
    path('api/borders/md/', BordersApiMdView.as_view(), ),
    path('api/borders/hi/', BordersApiHiView.as_view(), ),
]
