from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField(auto_now_add=True)
    bupd_date = models.DateField(auto_now=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgerder = models.BooleanField(default=0)
    hcomment = models.CharField(max_length=200, blank=True)
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'heroinfo'


class NewsType(models.Model):
    type_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'newstype'

class NewsInfo(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    news_type = models.ManyToManyField('NewsType')

    class Meta:
        db_table = 'newsinfo'

class EmployBasicInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.BooleanField(default=False)
    


class EmployDetailInfo(models.Model):
    addr = models.CharField(max_length=256)
    employee_basic = models.OneToOneField('EmployBasicInfo')



class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)
