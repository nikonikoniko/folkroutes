from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, Http404
from .models import *

def home(request):
  floatsam = Floatsam.objects.all()

  for sam in floatsam:
    sam.peers = sam.coven.all()
    if hasattr(sam, "constellation"):
      print ("ffffffffffffffffffffffffffffffffffffffffff")
      sam.charge = 2100
    else:
      sam.charge = -2000

  return render(request, 'homepage.html', {"floatsam":floatsam})


def directory(request):
  constellations = Constellation.objects.all()
  stars = Star.objects.all()
  jetsam = Jetsam.objects.all()
  floatsam = Floatsam.objects.all()

  for sam in floatsam:
    sam.peers = sam.coven.all()

  return render(request, 'directory.html', {"constellations":constellations,"stars":stars,"jetsam":jetsam,"floatsam":floatsam})


# Create your views here.
