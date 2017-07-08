# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
from filer.fields.image import FilerImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(upload_to="category")
    image = FilerImageField()

    def image_thumbnail(self):
        if self.image:
            s = '<img src="{src}" alt="{name}"/>'.format(src=self.image.thumbnails['admin_tiny_icon'], name=self.image.label)
            return mark_safe(s)
        else:
            return '(No image)'
    image_thumbnail.short_description = 'Thumb'

    def __unicode__(self):
        return self.name


class Video(models.Model):
    QUALITY_CHOICES = (
        (0, 'Normal'),
        (1, 'HD'),
    )
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, blank=True)
    poster = models.URLField()
    src = models.URLField()
    duration = models.IntegerField()
    quality = models.IntegerField(choices=QUALITY_CHOICES, default=0)

    def poster_thumbnail(self):
        if self.poster:
            poster_src = self.poster
            s = '<img src="{src}" alt="{name}" width="32" height="32"/>'.format(src=poster_src, name=self.name)
            return mark_safe(s)
        else:
            return '(No poster)'
    poster_thumbnail.short_description = 'Thumb'

    def __unicode__(self):
        return self.name

