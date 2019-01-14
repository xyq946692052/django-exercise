from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def login(request):
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        
        if 'username' in request.COOKIES and 'password' in request.COOKIES:
            username = request.COOKIES.get('username')
            password = request.COOKIES.get('password')
        else:
            username = ''
            password = ''
        return render(request, 'booktest/login.html', {'username':username, 'password':password})


def login_check(request):
    # get username and password
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
   
    print(username,password, remember)
    if username == 'admin' and password == '123':
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
            response.set_cookie('password', password, max_age=7*24*3600)
            # remember user the status of login
            request.session['islogin'] = True
        return response
    else:
        return redirect('/login')


def ajax_test(request):
    return render(request, 'booktest/ajax_test.html')


def ajax_handle(request):
     return JsonResponse({'res':1})

def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')

@csrf_exempt
def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    if username == 'admin' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def set_cookie(request):
    response = HttpResponse('set cookie')
    response.set_cookie('num', 1, max_age=14*24*3600)
    return response


def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    request.session['username'] = 'admin'
    request.session['age'] = 29
    return HttpResponse('set session')


def get_session(request):
    username = request.session.get('username')
    age = request.session.get('age')
    return HttpResponse(username+":"+str(age))
