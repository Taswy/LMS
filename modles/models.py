#coding=utf-8
from django.db import models
from django.utils import timezone
# Create your models here.

class Administor(models.Model):
    name = models.CharField(null=False,max_length=45)
    password = models.CharField(null=False,max_length=45)
    AUTHORITY_CHOICE = (('0','super'),('1','gene'))
    authority = models.CharField(max_length=1,choices=AUTHORITY_CHOICE,null=False) #权限

class Category(models.Model):
    name = models.CharField(null=False,max_length=45) #类型名称

class Books(models.Model):
    category = models.ForeignKey(Category) #类型
    title = models.CharField(null=False,max_length=45) #书名
    abstract = models.TextField(max_length=1000,null=False) #书籍简介
    stock = models.IntegerField(null=False,default=0) #库存量
    borrowed =  models.IntegerField(null=False,default=0) #借出数量
    indate = models.DateField(null=False) #入库日期

class Reader(models.Model):
    name = models.CharField(null=False,max_length=45)
    SEX_CHOICE = (('0','m'),('1','f'))
    sex = models.CharField(max_length=1,null=False,choices=SEX_CHOICE)
    rtype = models.CharField(null=False,max_length=45) #读者类型
    bar_code = models.CharField(null=False,max_length=45) #条形码
    birthday = models.DateField(null=False)
    paper_type = models.CharField(null=False,max_length=45) #证件类型
    paper_number = models.CharField(null=False,max_length=45) #证件号
    Email = models.EmailField(null=False)
    phonenumber = models.CharField(max_length=45)

class Recoders(models.Model):
    reader = models.ForeignKey(Reader)
    book = models.ForeignKey(Books)
    lend_date = models.DateField(null=False) #借出日期
    return_date = models.DateField(blank=True,null=True) #归还日期
    STATUS_CHOICE = (('0','lend'),('1','return'),('2','exceed'))
    status = models.CharField(max_length=1,choices=STATUS_CHOICE,null=False) #借阅状态：借出，已归还，超期
    limit = models.IntegerField(default=90) #借阅期限


