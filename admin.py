from django.contrib import admin
from django.contrib.gis.forms.widgets import OSMWidget
from django.contrib.gis.db import models

from .models import Border

@admin.register(Border)
class BorderAdmin(admin.ModelAdmin):
    list_display = ('name', )
    formfield_overrides = {
        models.GeometryField: {"widget": OSMWidget},
    }
