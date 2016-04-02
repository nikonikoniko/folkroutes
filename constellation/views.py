from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import JsonResponse

from django.core.exceptions import PermissionDenied

from .models import *
from .forms import *


def home(request):
  floatsam = Floatsam.objects.all()
  try:
    current_star=Star.objects.get(id=request.user.id)
    edit_array = current_star.can_edit_array
  except:
    current_star=None
    edit_array=[]

  for sam in floatsam:
    sam.peers = sam.coven.all()
    if hasattr(sam, "constellation"):
      sam.charge = -300
    else:
      sam.charge = -2000
  return render(request, 'homepage.html', {"floatsam":floatsam, "editable_slugs":edit_array})


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
  floatsamjson["jetsam"] = [x.json for x in floatsam.jetsam_set.all()]
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


def check_perms(request, slug):
  current_star =Star.objects.get(id=request.user.id)
  if slug in current_star.can_edit_array:
      pass
  else:
    raise PermissionDenied("No perms to do that")



@login_required
def add_jetsam(request, slug=None, makerslug=None):

  try:
    jetsam = Jetsam.objects.get(slug=slug)
  except:
    jetsam = None

  current_star=Star.objects.get(id=request.user.id)

  if jetsam:
    check_perms(request, jetsam.maker.slug)

  if makerslug:
    maker = get_object_or_404(Floatsam, slug=makerslug)
  else:
    maker = current_star


  if not jetsam and request.method == 'GET':
      form = JetsamAddForm()
  elif jetsam and request.method == 'GET':
    form = JetsamAddForm(instance=jetsam)
  else:
      if jetsam:
        form = JetsamAddForm(request.POST, instance=jetsam)
      else:
        form = JetsamAddForm(request.POST)

      if form.is_valid():

        newjet = form.save(commit=False)
        newjet.maker = maker

        print (request.FILES)

        if request.FILES.get("upload"):
          newjet.upload = request.FILES["upload"]

        newjet.save()

        return redirect('add_jetsam', slug=newjet.slug, makerslug=maker.slug)

  submit_url = reverse("add_jetsam", args={
    slug, maker.slug,
    })

  return render(request, 'constellation/generic_form.html', {
      'form': form, 'submit_url':submit_url,
  })



@login_required
def edit_floatsam(request, slug=None):

  floatsam = get_object_or_404(Floatsam, slug=slug)

  form = FloatsamEditForm(instance=floatsam)

  check_perms(request, floatsam.slug)

  if request.method == 'POST':
    form = FloatsamEditForm(request.POST, instance=floatsam)
    if form.is_valid():
      newfloat = form.save(commit=False)
      if request.FILES.get("vanity_image"):
        newfloat.vanity_image = request.FILES["vanity_image"]
      newfloat.save()
  else:
    form = FloatsamEditForm(instance=floatsam)


  submit_url = reverse("edit_floatsam", args={
    slug,
    })

  return render(request, 'constellation/generic_form.html', {
      'form': form, 'submit_url':submit_url,
  })


@login_required
def request_floatsam(request, slug=None):
  recipient     = get_object_or_404(Floatsam, slug=slug)
  initiator     = Star.objects.get(id=request.user.id)
  connection    = ConnectionRequest.objects.get_or_create(initiator=initiator, recipient=recipient)
  return HttpResponse("connection requested")

@login_required
def accept_request(request, initiator_slug=None, recipient_slug=None):
  check_perms(request, recipient_slug)
  initiator     = get_object_or_404(Floatsam, slug=initiator_slug)
  recipient     = get_object_or_404(Floatsam, slug=recipient_slug)
  connection    = get_object_or_404(ConnectionRequest, initiator=initiator, recipient=recipient)
  try:
    ConnectionRequest.objects.get(initiator=recipient, recipient=initiator).delete()
  except:
    pass
  initiator.coven.add(recipient)
  initiator.save()
  connection.delete()
  return HttpResponse("connection added!")


@login_required
def deny_request(request, initiator_slug=None, recipient_slug=None):
  check_perms(request, recipient_slug)
  initiator     = get_object_or_404(Floatsam, slug=initiator_slug)
  recipient     = get_object_or_404(Floatsam, slug=recipient_slug)
  connection    = get_object_or_404(ConnectionRequest, initiator=initiator, recipient=recipient)
  connection.delete()
  return HttpResponse("connection deleted")


