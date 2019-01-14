from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, HeroInfo
# Create your views here.



def index(request):
    context = {'message':'hello xyq'}
    context.update({'lst':['python', 'django', 'redis', 'kafka']})
    return render(request, 'booktest/index.html',context)



def books(request):
    context = {}
    book_obj = BookInfo.objects.all()
    context['books'] = book_obj
 
    return render(request, 'booktest/books.html', context) 


def detail(request, book_id):
    context = {}
    book = BookInfo.objects.get(id=book_id)
    heros = book.heroinfo_set.all()
    context['book'] =  book
    context['heros'] = heros
    return render(request, 'booktest/detail.html', context)
