from django.contrib import admin

from .models import *
from .forms import *



class SecondUserAdmin(UserAdmin):
  add_form = SecondUserAddForm
  form = SecondUserChangeForm

  list_display = ("email", "created_at", "updated_at")
  list_filter = ("created_at","updated_at")
  search_fields = ("email",)
  ordering = ("created_at","email",)
  filter_horizontal = ()
  fieldsets = (
    (None,{"fields":("email","password",)}),
    )
  add_fieldsets = ((None, {
    "fields":("email","password1","password2")
    }), )

admin.site.register(SecondUser, SecondUserAdmin)
