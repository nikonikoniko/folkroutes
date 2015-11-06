from django.db import models
from seconduser.models import SecondUser
from djgeojson.fields import PointField, PolygonField


class Floatsam(models.Model):
  floatsam_id   = models.AutoField(primary_key=True)
  coven         = models.ManyToManyField("self")
  geom          = PointField(null = True, blank = True)


class Nameable(models.Model):
  name      = models.CharField(max_length=255)
  website   = models.CharField(max_length=255, null = True, blank = True)
  story     = models.TextField(null = True, blank = True)
  class Meta:
    abstract = True


class Constellation(Floatsam, Nameable):
  pass


class Star(SecondUser, Floatsam, Nameable):
  pass





