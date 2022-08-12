from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Page


def index(request):
    latest_pages_list = Page.objects.order_by("-pub_date")
    return render(request, "pages/list.html", {"latest_pages_list": latest_pages_list})


def detail(request, page_id):
    try:
        a = Page.objects.get(id=page_id)
    except:
        raise Http404("Запись не найдена")
    return render(request, "pages/detail.html", {"page": a})
