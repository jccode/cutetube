# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "tubesite/index.html")


def video_detail(request, id):
    return render(request, "tubesite/video.html")


def categories(request):
    return render(request, "tubesite/categories.html")


def category(request, id):
    return render(request, "tubesite/category.html")
