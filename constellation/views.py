from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import *
from .forms import *


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
  floatsam = get_object_or_404(Floatsam, slug=slug)
  floatsam.peers = floatsam.coven.all()
  ct = ContentType.objects.get_for_model(Constellation)
  constellations = []
  return render(request, 'constellation/floatsam_detail.html',{"floatsam":floatsam,"constellations":constellations})

def json_floatsam_detail(request, slug):
  floatsam = get_object_or_404(Floatsam, slug=slug)
  floatsamjson = floatsam.json
  return JsonResponse(floatsamjson)


def links_json(request):
  floatsam = Floatsam.objects.all()

  for sam in floatsam:
    sam.peers = sam.coven.all()
    if hasattr(sam, "constellation"):
      sam.charge = -300
    else:
      sam.charge = -2000

  links = [{"source": item.floatsam_id, "target":  thing.floatsam_id}
    for thing in floatsam
      for item in floatsam
        if item.floatsam_id in [x.floatsam_id for x in thing.peers]
        ]

  links = [dict(y) for y in set(tuple(x.items()) for x in links)]

  return JsonResponse(links, safe=False)

def floatsam_json(request):
  floatsam = Floatsam.objects.all()
  floatsam_list=[{"num":0,"name":"FolkRoutes","charge":-200},]
  for item in floatsam:
    if hasattr(item, "constellation"):
      item.charge = -300
    else:
      item.charge = -2000
    print (item.name)
    floatsam_list.append({
            "num":item.floatsam_id,
            "name":item.name,
            "url":"/floatsam/json/"+item.slug,
            "charge":item.charge,
      })
  return JsonResponse(floatsam_list, safe=False)


@login_required
def add_jetsam(request, slug=None):

  try:
    jetsam = Jetsam.objects.get(slug=slug)
  except:
    jetsam = None

  current_star=Star.objects.get(id=request.user.id)
  if jetsam:
    if jetsam.maker.floatsam_id in [x.floatsam_id for x in current_star.coven.all()] or jetsam.maker.floatsam_id == current_star.floatsam_id:
      print ("woooo")
    else:
      return HttpResponse("No perms to do that")


  if not jetsam and request.method == 'GET':
      form = JetsamAddForm()
  elif jetsam and request.method == 'GET':
    print ("in here")
    form = JetsamAddForm(instance=jetsam)
  else:
      if jetsam:
        form = JetsamAddForm(request.POST, instance=jetsam)
      else:
        form = JetsamAddForm(request.POST)

      if form.is_valid():
        print (form)
        newjet = form.save(commit=False)
        newjet.maker = current_star
        newjet.save()

        print ("yay!")
        return redirect('add_jetsam', slug=newjet.slug)
  return render(request, 'constellation/add_jetsam.html', {
      'form': form, 'slug':slug,
  })