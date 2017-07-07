# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from services import get_category_all_count, get_popular_categories
# Create your views here.


def index(request):
    return render(request, "tubesite/index.html")


def video_detail(request, id):
    return render(request, "tubesite/video.html")


def categories(request):
    context = {
        "categories_all_count": get_category_all_count(),
        "popular_categories": get_popular_categories()
    }
    return render(request, "tubesite/categories.html", context)


def category(request, id):
    context = {
        "categories_all_count": get_category_all_count()
    }
    return render(request, "tubesite/category.html", context)


def about(request):
    return render(request, "tubesite/info.html")
