# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db.models import Count
from models import Video, Category


def category_count():
    return Video.objects.values("category").annotate(count=Count("category"))


def categories_with_count():
    """Get categories with count from cache"""
    return cache.get_or_set("categories_with_count", lambda: _categories_with_count())


def _categories_with_count():
    """Get categories with count"""
    cats = cache.get("categories")
    if cats is None:
        cats = Category.objects.all().values()
    c_counts = {c['category']: c['count'] for c in category_count()}
    for cat in cats:
        cat['count'] = c_counts[cat['id']] if c_counts.has_key(cat['id']) else 0
    return cats