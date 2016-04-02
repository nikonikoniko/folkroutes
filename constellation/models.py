from django.db import models
from seconduser.models import SecondUser
from djgeojson.fields import PointField, PolygonField
from stdimage.models import StdImageField
from autoslug import AutoSlugField






class Nameable(models.Model):
  name      = models.CharField(max_length=255)
  website   = models.CharField(max_length=255, null = True, blank = True)
  story     = models.TextField(null = True, blank = True)
  slug      = AutoSlugField(populate_from='name', unique=True, always_update=True)

  class Meta:
    abstract = True

class Imageable(models.Model):
  vanity_image = StdImageField(upload_to="vanity_image", blank=True, variations={
        'large': (800, 800),
        'thumbnail': (100, 100),
        'medium': (300, 300),
    })
  @property
  def image(self):
    if self.vanity_image:
      return self.vanity_image
    else:
      return "none"

  @property
  def imageurl(self):
    if self.vanity_image:
      return self.vanity_image.medium.url
    else:
      return "none"


  class Meta:
    abstract = True


# jetsam is a production of one of these nodes
class Jetsam(Nameable):
  maker         = models.ForeignKey("Floatsam")
  upload        = models.FileField(upload_to="jetsam", null=True, blank=True)
  summary       = models.TextField(null = True, blank = True)
  TYPES = (
    (1, "Writing"),
    (2, "Audio"),
    (3, "Image"),
    (4, "Document"))
  type = models.IntegerField(choices=TYPES, default=1)

  @property
  def upload_url(self):
    if self.upload:
      return self.upload.url
    else:
      return None



  @property
  def json(self):
    return {
        "name":self.name,
        "story":self.story,
        "type":self.type,
        "slug":self.slug,
        "maker":self.maker.name,
        "upload":self.upload_url,
        "maker_slug":self.maker.slug,

        }


# floatsam is a node on the network, a connecting point (project) or a human
class Floatsam(Nameable, Imageable):
  floatsam_id   = models.AutoField(primary_key=True)
  coven         = models.ManyToManyField("self", blank=True)
  geom          = PointField(null = True, blank = True)

  @property
  def json(self):
      return {
        "floatsam_id":self.floatsam_id,
        "coven":[x.name for x in self.coven.all()],
        "name":self.name,
        "story":self.story,
        "website":self.website,
        "image":self.imageurl,
        "slug":self.slug,
      }



  def __str__(self):
    return self.name

class Constellation(Floatsam):
  def __str__(self):
    return self.name


class Star(SecondUser, Floatsam):
  @property
  def can_edit_array(self):
      peers = []
      for peer in self.coven.all():
        if hasattr(peer, "constellation"):
          peers.append(peer)
      return [x.slug for x in peers] + [self.slug]

  def __str__(self):
    return self.name



class ConnectionRequest(models.Model):
  initiator = models.ForeignKey("Floatsam", related_name="initiator")
  recipient = models.ForeignKey("Floatsam", related_name="recipient")

  def __str__(self):
    return self.initiator.name + " > " + self.recipient.name



