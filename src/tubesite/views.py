# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.forms.models import model_to_dict
from .services import get_category_all_count, get_popular_categories
from .models import Video
import logging


# Create your views here.

logger = logging.getLogger(__name__)
PAGE_SIZE = 20


def index(request):
    return render(request, "tubesite/index.html")


def video_detail(request, id):
    context = {
        "video": model_to_dict(Video.objects.get(pk=id))
    }
    return render(request, "tubesite/video.html", context)


def categories(request):
    context = {
        "categories_all_count": get_category_all_count(),
        "popular_categories": get_popular_categories()
    }
    return render(request, "tubesite/categories.html", context)


def category(request, id):
    video_list = Video.objects.all() if id == '0' else Video.objects.filter(category=id)
    paginator = Paginator(video_list, PAGE_SIZE)
    page = request.GET.get("page", 1)

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        videos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        videos = paginator.page(paginator.num_pages)

    context = {
        "categories_all_count": get_category_all_count(),
        "videos": videos,
    }
    return render(request, "tubesite/category.html", context)


def about(request):
    return render(request, "tubesite/info.html")
