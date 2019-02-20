from django.shortcuts import render, HttpResponse



def index(request):
    return render(request, 'mainsite/index.html')



def login(request):
   return render(request, 'mainsite/login.html') 


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('---------',username, password)
    return HttpResponse('<h1>Success</h1>')
