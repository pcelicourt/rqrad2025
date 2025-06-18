from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import SamplingFeatures

@admin.register(SamplingFeatures)
class SamplingFeaturesAdmin(GISModelAdmin):
    list_display = ('samplingfeaturetypecv', 'featuregeometry', 'samplingfeaturename')