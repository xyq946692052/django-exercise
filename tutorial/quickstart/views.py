# -*- encoding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''允许用户查看或编辑的API路径'''
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''允许用户查看或编辑的API 路径'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

