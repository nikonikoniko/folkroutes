from django.db import models
from seconduser.models import SecondUser
from djgeojson.fields import PointField, PolygonField
from stdimage.models import StdImageField





class Nameable(models.Model):
  name      = models.CharField(max_length=255)
  website   = models.CharField(max_length=255, null = True, blank = True)
  story     = models.TextField(null = True, blank = True)

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

# floatsam is a node on the network, a connecting point (project) or a human
class Floatsam(Nameable, Imageable):
  floatsam_id   = models.AutoField(primary_key=True)
  coven         = models.ManyToManyField("self")
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
      }



  def __str__(self):
    return self.name

class Constellation(Floatsam):
  def __str__(self):
    return self.name


class Star(SecondUser, Floatsam):
  def __str__(self):
    return self.name





