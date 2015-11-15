from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .models import *
from django.contrib.contenttypes.models import ContentType
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http import JsonResponse

def home(request):
  floatsam = Floatsam.objects.all()

  for sam in floatsam:
    sam.peers = sam.coven.all()
    if hasattr(sam, "constellation"):
      sam.charge = -300
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


def floatsam_detail(request, slug):
  floatsam = get_object_or_404(Floatsam, pk=slug)
  floatsam.peers = floatsam.coven.all()
  ct = ContentType.objects.get_for_model(Constellation)
  constellations = []#Floatsam.objects.filter(content_type__model="Constellation")
  print ("ooooooooooooo")
  print (floatsam)
  print (")yyyyyyy")
  return render(request, 'constellation/floatsam_detail.html',{"floatsam":floatsam,"constellations":constellations})

def json_floatsam_detail(request, slug):
  floatsam = get_object_or_404(Floatsam, pk=slug)
  floatsamjson = floatsam.json
  return JsonResponse(floatsamjson)