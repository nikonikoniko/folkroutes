from django.contrib import admin

from .models import *
from seconduser.forms import *

from leaflet.admin import LeafletGeoAdmin



class ConstellationAdmin(admin.ModelAdmin):
  pass


class JetsamAdmin(admin.ModelAdmin):
  pass

class ConnectionRequestAdmin(admin.ModelAdmin):
  pass

class StarAdmin(UserAdmin, LeafletGeoAdmin):
  add_form = SecondUserAddForm

  list_display = ("name", "email", "created_at", "updated_at")
  list_filter = ("created_at","updated_at")
  search_fields = ("email",)
  ordering = ("created_at","email",)
  filter_horizontal = ()
  fieldsets = (
    (None,{"fields":("email","password","name","story","website","coven","geom","vanity_image")}),
    )
  add_fieldsets = ((None, {
    "fields":("email","password1","password2")
    }), )

  class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    )
    css = {
    }

admin.site.register(Star, StarAdmin)
admin.site.register(Constellation, ConstellationAdmin)
admin.site.register(Jetsam, JetsamAdmin)
admin.site.register(ConnectionRequest, ConnectionRequestAdmin)