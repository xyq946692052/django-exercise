from django.shortcuts import render, redirect
from django.http import HttpResponse
from booktest.models import BookInfo, AreaInfo
from datetime import date
# Create your views here.


def books(request):
    context = {}
    bookobjs = BookInfo.objects.all()
    context['bookobjs'] = bookobjs
    return render(request, 'booktest/books.html', context)


def create(request):
    b = BookInfo()
    b.btitle = "Ken"
    b.bpub_date = date(1990,12,10)
    b.save()
    return redirect('/books')


def delete(request, bid):
    b = BookInfo.objects.get(id=bid)
    b.delete()
    return redirect('/books')
    

def areas(request):
    area = AreaInfo.objects.get(atitle='SZ')
    parent = area.aParent
    children = area.areainfo_set.all()
    return render(request, 'booktest/areas.html', {'area':area, 'parent': parent,'children':children})
