from django.contrib import admin

from .models import *
from seconduser.forms import *

from leaflet.admin import LeafletGeoAdmin



class ConstellationAdmin(admin.ModelAdmin):
  pass


class StarAdmin(LeafletGeoAdmin):
  pass

admin.site.register(Star, StarAdmin)
admin.site.register(Constellation, ConstellationAdmin)