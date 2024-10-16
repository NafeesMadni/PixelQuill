from pixelquill.utils import categories

def category_context(request):
    return {
        'categories':  categories,
    }
