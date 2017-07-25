from .services import get_categories


def categories(request):
    # Should get from cache first
    context = {'categories': get_categories()}
    return context
