from django.forms import ModelForm
from .models import Jetsam, Floatsam
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class JetsamAddForm(ModelForm):
  form_title="Add Jetsam"
  form_url_name = "add_jetsam"
  class Meta:
    model = Jetsam
    exclude = ['maker']
    widgets = {
            'story': SummernoteWidget(),
        }

class FloatsamEditForm(ModelForm):
  form_title="Edit Floatsam"
  form_url_name = "edit_floatsam"
  class Meta:
    exclude = ['slug','coven','geom']
    model = Floatsam
    widgets = {
            'story': SummernoteWidget(),
        }

