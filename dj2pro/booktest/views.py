# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from django.utils.six import BytesIO
from django.conf import settings
from django.core.paginator import Paginator
from PIL import Image, ImageDraw, ImageFont
from booktest.models import BookInfo, PicTest, AreaInfo


# Create your views here.

def login_required(func):
    def wrapper(request, *kw, **kwargs):
        if request.session.has_key('islogin'):
            return func(request, *kw, **kwargs)
        else:
            return redirect('/login')

    return wrapper


def index(request):
    print('----------index-----------')
    client_ip = request.META['REMOTE_ADDR']
    return render(request, 'booktest/index.html', {'client_ip': client_ip})


def temp_var(request):
    context = {}
    my_dict = {'title': 'keyval'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.all()
    context['my_dict'] = my_dict
    context['my_list'] = my_list
    context['book'] = book
    return render(request, 'booktest/temp_var.html', context)


def temp_tag(request):
    books = BookInfo.objects.all()
    context = {}
    context['books'] = books
    return render(request, 'booktest/temp_tag.html', context)


def temp_filter(request):
    books = BookInfo.objects.all()
    context = {}
    context['books'] = books
    return render(request, 'booktest/temp_filter.html', context)


def login(request):
    if request.session.has_key('islogin'):
        return redirect('/change_pwd')
    else:

        if 'username' in request.COOKIES and 'password' in request.COOKIES:
            username = request.COOKIES.get('username')
            password = request.COOKIES.get('password')
        else:
            username = ''
            password = ''
        return render(request, 'booktest/login.html', {'username': username, 'password': password})


def login_check(request):
    # get username and password
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 获取用户输入的验证码
    vcode = request.POST.get('vcode')
    # 获取session中保存的验证码
    vcode2 = request.session.get('verifycode')
    if vcode != vcode2:
        return redirect('/login')
    print(username, password, remember)
    if username == 'admin' and password == '123':
        response = redirect('/change_pwd')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
            response.set_cookie('password', password, max_age=7 * 24 * 3600)
            # remember user the status of login
            request.session['islogin'] = True
            request.session['username'] = username
        return response
    else:
        return redirect('/login')


@login_required
def change_pwd(request):
    return render(request, 'booktest/change_pwd.html', {})


@login_required
def change_pwd_action(request):
    pwd = request.POST.get('pwd')
    username = request.session.get('username')
    return HttpResponse('{} 修改密码为:{} '.format(username, pwd))


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量， 用于画面的背景色，宽，高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point（）函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    strl = 'ABCD123EFGHIJK456LMNOPQRS789TUVMXYZ0'
    rand_str = ''
    for i in range(0, 4):
        rand_str += strl[random.randrange(0, len(strl))]
    # 构造字体对象,
    font = ImageFont.truetype('static/font/SIMLI.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制四个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session,用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存进内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回到客户端，MIMEpng
    return HttpResponse(buf.getvalue(), 'image/png')


# 用户上传文件
def show_upload(request):
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    # 1、获取上传文件的处理对象
    pic = request.FILES['pic']
    # 2、创建保存的路径
    save_path = '{}/booktest/{}'.format(settings.MEDIA_ROOT, pic.name)

    with open(save_path, 'wb') as f:
        # 3、获取上传文件的内容， 并写到创建的文件中
        for content in pic.chunks():  # pic.chunks文件内容
            f.write(content)

    # 4、数据库中保存上传记录
    PicTest.objects.create(
        goods_pic='booktest/{}'.format(pic.name)
    )
    # 5、返回
    return redirect('/show_imgs')


def show_imgs(request):
    context = {}
    picobjs = PicTest.objects.all()
    context['picobjs'] = picobjs
    return render(request,'booktest/show_imgs.html', context)


def show_area(request, num):
    areas = AreaInfo.objects.filter(aParent__isnull=False)
    paginator = Paginator(areas, 10)
    if num == '':
        num = 1
    page = paginator.page(int(num))
    page_range = page.paginator.page_range

    current_page = page.number
    if paginator.num_pages > 12:
        if current_page < 10:
            print('-------------1')
            page_range = page_range[:10]
        elif  10<= current_page <= paginator.num_pages-10:
            print('-----------2')
            page_range = page_range[current_page-5:current_page+5]
        else:
            print('---------3')
            page_range = page_range[paginator.num_pages-10:]
        print('++++++++++', page_range)

    return render(request, 'booktest/show_area.html', {'page': page, 'page_range': page_range})
