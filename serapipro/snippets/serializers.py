# /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICE, PicFile

# 1、方式一
# class SnippetSerializer_bak(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     lineos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICE, default='friendly')
#
#     def create(self, validated_data):
#         """根据提供的验证过的数据创建并返回一个新的Snippet实例"""
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """根据提供的验证过的数据更新和返回一个已经存在的Snippet实例"""
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#        return instance


# 2、最简最优方式
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'lineos', 'language', 'style', 'owner')



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')



class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicFile
        fields = ('id', 'pic')