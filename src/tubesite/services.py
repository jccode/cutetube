# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db.models import Count
from .models import Video, Category
import random


CACHE_KEY_CATEGORIES = "categories"
CACHE_KEY_CATEGORY_ALL_COUNT = "category_all_count"


def get_categories():
    cats = cache.get(CACHE_KEY_CATEGORIES)
    if cats is not None:
        return cats
    else:
        cats = Category.objects.all()
        counts = Video.objects.values("category").annotate(count=Count("category"))
        count_dict = {c['category']: c['count'] for c in counts}
        for c in cats:
            cid = c.id
            c.count = count_dict[cid] if cid in count_dict else 0

        # set cats to cache
        cache.set(CACHE_KEY_CATEGORIES, cats)
        cache.set(CACHE_KEY_CATEGORY_ALL_COUNT, sum(count_dict.values()))

        return cats


def get_category_all_count():
    count = cache.get(CACHE_KEY_CATEGORY_ALL_COUNT)
    if count is not None:
        return count
    else:
        count = Video.objects.count()
        # save to cache
        cache.set(CACHE_KEY_CATEGORY_ALL_COUNT, count)
        return count


def get_popular_categories():
    return cache.get_or_set("popular_categories", lambda: _get_popular_categories())


# TODO to be correct the business
def _get_popular_categories():
    cats = get_categories()
    if len(cats) <= 4:
        return cats
    else:
        return random.sample(list(cats), 4)
