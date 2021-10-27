from django.urls import path

from .views import *

app_name = 'maps'
urlpatterns = [
    path('', BordersMapView.as_view(), name = 'borders'),
]
