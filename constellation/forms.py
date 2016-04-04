from django.forms import ModelForm
from .models import Jetsam, Floatsam, Constellation
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_bleach.forms import BleachField

class JetsamAddForm(ModelForm):
  form_title="Add Jetsam"
  #form_url_name = "add_jetsam"
  class Meta:
    model = Jetsam
    exclude = ['maker']
    fields = ['type', 'name' , 'summary', 'upload', 'story','website']
    widgets = {
            'story': SummernoteWidget(),
        }

class FloatsamEditForm(ModelForm):
  form_title="Edit Floatsam"
  story=BleachField(allowed_tags=[
        'p', 'b', 'i', 'u', 'em', 'strong', 'a',
        'img','h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
        allowed_styles=[],allowed_attributes=['href', 'title'])
  #form_url_name = "edit_floatsam"
  class Meta:
    exclude = ['slug','coven','geom']
    model = Floatsam
    widgets = {
            'story': SummernoteWidget(),
        }


class ConstellationAddForm(FloatsamEditForm):
  form_title="Add Floatsam"
  class Meta:
    exclude = ['slug','coven','geom']
    model = Constellation
    widgets = {
            'story': SummernoteWidget(),
        }