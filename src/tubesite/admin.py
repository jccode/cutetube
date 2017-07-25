# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Video

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'name', 'image')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('poster_thumbnail', 'name', 'category', 'duration', 'quality')
    list_display_links = ('poster_thumbnail', 'name')


