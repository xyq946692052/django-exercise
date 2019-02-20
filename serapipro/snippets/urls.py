# /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('', views.api_root),
    path('snippets/<int:num>/highlight/', views.SnippetHighlight.as_view()),
    path('pics', views.PicList.as_view()),
    path('pics/<int:pk>', views.PicDetail.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

urlpatterns = format_suffix_patterns(urlpatterns)
