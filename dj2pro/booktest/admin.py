from django.contrib import admin
from booktest.models import AreaInfo, PicTest
import xadmin


#使用自带的admin
# # Register your models here.
# class AreaStackedInline(admin.StackedInline):
#     # 写多类的名字
#     model = AreaInfo
#
#
# class AreaTabularInline(admin.TabularInline):
#     model = AreaInfo
#
#
# # 嵌入的表格类型
# class AreaInfoAdmin(admin.ModelAdmin):
#     list_per_page = 10  # 每页显示10条数据
#     list_display = ['id', 'atitle', 'parent']
#     list_filter = ['atitle']  # 页表页过滤栏
#     search_fields = ['atitle']  # 添加搜索框
#
#     # fields = ['aParent', 'atitle']  # 显示字段顺序
#     fieldsets = (  # fields 和 fieldsets只能二选一
#         ('基本', {'fields': ['atitle']}),
#         ('高级', {'fields': ['aParent']}),
#     )
#     inlines = [AreaStackedInline]
#     # inlines = [AreaTabularInline]
#
#
# class PicTestAdmin(admin.ModelAdmin):
#     list_display = ['id', 'goods_pic']
#
#
# admin.site.register(AreaInfo, AreaInfoAdmin)
# admin.site.register(PicTest, PicTestAdmin)

# 使用xadmin方式
class AreaInfoAdmin(object):
    list_display = ['id', 'atitle', 'parent']
    search_fields = ['atitle']
    list_filter = ['atitle']


class PicTestAdmin(object):
    list_display = ['id', 'goods_pic']


xadmin.site.register(AreaInfo, AreaInfoAdmin)
xadmin.site.register(PicTest, PicTestAdmin)