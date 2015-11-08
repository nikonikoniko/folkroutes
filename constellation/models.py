from django.db import models
from seconduser.models import SecondUser
from djgeojson.fields import PointField, PolygonField





class Nameable(models.Model):
  name      = models.CharField(max_length=255)
  website   = models.CharField(max_length=255, null = True, blank = True)
  story     = models.TextField(null = True, blank = True)

  class Meta:
    abstract = True


# jetsam is a production of one of these nodes
class Jetsam(Nameable):
  maker         = models.ForeignKey("Floatsam")

# floatsam is a node on the network, a connecting point (project) or a human
class Floatsam(Nameable):
  floatsam_id   = models.AutoField(primary_key=True)
  coven         = models.ManyToManyField("self")
  geom          = PointField(null = True, blank = True)

  def __str__(self):
    return self.name

class Constellation(Floatsam):
  def __str__(self):
    return self.name


class Star(SecondUser, Floatsam):
  def __str__(self):
    return self.name





