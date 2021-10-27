from django.urls import path

from .api_views import *

app_name = 'map_api'
urlpatterns = [
    path('borders/lo/', BordersApiLoView.as_view(), ),
    path('borders/md/', BordersApiMdView.as_view(), ),
    path('borders/hi/', BordersApiHiView.as_view(), ),
    path('borders/full/', BordersApiView.as_view(), ),
]
