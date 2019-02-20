from django.contrib import admin
from .models import PicFile
# Register your models here.

class PicFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic')

admin.site.register(PicFile, PicFileAdmin)
