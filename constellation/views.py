from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, Http404
from .models import *

def home(request):
  constellations = Constellation.objects.all()
  stars = Star.objects.all()
  jetsam = Jetsam.objects.all()
  floatsam = Floatsam.objects.all()
  print (floatsam.__dict__)
  print (floatsam[0].__dict__)
  print (floatsam[0].coven)

  for sam in floatsam:
    sam.peers = sam.coven.all()

  return render(request, 'homepage.html', {"constellations":constellations,"stars":stars,"jetsam":jetsam,"floatsam":floatsam})



# Create your views here.
