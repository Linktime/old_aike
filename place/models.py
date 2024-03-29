from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.

class Lbs(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    def __unicode__(self):
        return "%f--%f"%(self.lat,self.lng)

class Province(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    pid = models.IntegerField()
    lever = models.IntegerField()

    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region)

class GenericPlace(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

class UniversityType(models.Model):
    type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.type

class UniversityBelongTo(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class University(models.Model):
    district = models.ForeignKey(Province)
    name = models.CharField(max_length=30)
    type = models.ForeignKey(UniversityType)
    belong_to = models.ForeignKey(UniversityBelongTo)
    def __unicode__(self):
        return self.name