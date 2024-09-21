from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Urban.task2.models import *


# Create your views here.
def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    elements_per_page = request.GET.get('elements_per_page', 3)
    paginator = Paginator(posts, per_page=elements_per_page)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'elements_per_page': elements_per_page
    }
    return render(request, 'index.html', context)
# Create your views here.
