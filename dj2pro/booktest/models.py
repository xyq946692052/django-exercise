from django.db import models


# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column='title')
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)

    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20, verbose_name="地区名")
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=True)

    def __str__(self):
        return self.atitle

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle

    atitle.admin_order_filed = 'atitle'
    parent.short_description = '父级地名'  # admin页面列名

    class Meta:
        db_table = 'booktest_areainfo'


class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='booktest')
