from django.forms import ModelForm
from .models import Jetsam

class JetsamAddForm(ModelForm):
  class Meta:
    model = Jetsam
    exclude = ['maker']