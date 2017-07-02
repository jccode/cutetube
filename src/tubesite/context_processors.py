from django.core.cache import cache
from models import Category


def categories(request):
    # Should get from cache first
    cats = cache.get_or_set("categories", lambda: Category.objects.all())
    context = {'categories': cats}
    return context
