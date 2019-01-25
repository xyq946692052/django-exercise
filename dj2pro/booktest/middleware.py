# -*-encoding:utf-8 -*-
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPMiddleware(MiddlewareMixin):
    BLOCK_IPS = ['192.168.191.1']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """试图函数调用前会调用 """
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in self.BLOCK_IPS:
            return HttpResponse("<h1>Forbbin</h1>")


class TestMiddleware(MiddlewareMixin):
    def __init__(self,get_response):
        """服务器重启之后，接受第一个请求时调用"""
        print('---------__init__--------')
        self.get_response = get_response

    def process_request(self, request):
        """产生request对象，进行url匹配前调用"""
        print('-----process_request-------')

    def process_view(self, request, view_func, *view_args, **kwargs):
        """url匹配后，试图函数调用之前调用"""
        print('------process_view--------')

    def process_response(self, request, response):
        """试图函数调用之后，内容返回浏览器之前调用"""
        print('-------process_response-----')
        return response


class ExceptionTest1Middleware(MiddlewareMixin):
    def process_exception(self,request, exception):
        '''视图函数发生异常时调用'''
        print('-------process_exception-1------', exception)


class ExceptionTest2Middleware(MiddlewareMixin):
    def process_exception(self,request, exception):
        '''视图函数发生异常时调用'''
        print('-------process_exception-2------')