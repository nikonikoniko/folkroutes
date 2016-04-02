from django.forms import ModelForm
from .models import Jetsam, Floatsam

class JetsamAddForm(ModelForm):
  form_title="Add Jetsam"
  form_url_name = "add_jetsam"
  class Meta:
    model = Jetsam
    exclude = ['maker']

class FloatsamEditForm(ModelForm):
  form_title="Edit Floatsam"
  form_url_name = "edit_floatsam"
  class Meta:
    exclude = ['slug','coven']
    model = Floatsam
