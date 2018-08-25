from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from myapps.art.models import Art


@cache_page(10)
def show(request,artid):

    # 查看指定文章
    art = Art.objects.get(artid)

