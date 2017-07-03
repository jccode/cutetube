# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from services import categories_with_count
# Create your views here.


def index(request):
    return render(request, "tubesite/index.html")


def video_detail(request, id):
    return render(request, "tubesite/video.html")


def categories(request):
    context = {
        "categories_with_count": categories_with_count()
    }
    return render(request, "tubesite/categories.html", context)


def category(request, id):
    context = {
        "categories_with_count": categories_with_count()
    }
    return render(request, "tubesite/category.html", context)


def about(request):
    return render(request, "tubesite/info.html")
