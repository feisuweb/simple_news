#coding:utf-8
from django.db import models
import hashlib

class MyUser(models.Model):
    """
    用户
    """
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 50)
    email = models.EmailField()
    create_time = models.DateTimeField(auto_now_add=True)
    usergroup = models.ForeignKey('MyGroup',default = 1)

    def hashed_password(self, password=None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        return False

    def __str__(self):
        return self.username

class MyGroup(models.Model):
    """
    用户组
    """
    groupname = models.CharField(max_length = 20)

    def __str__(self):
        return self.groupname

class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length = 20)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length = 20)#标题
    body = models.TextField()#正文
    pub_user = models.CharField(max_length = 20)#发布用户
    create_time = models.DateTimeField(auto_now_add = True)#发布时间
    update_time = models.DateTimeField(auto_now = True)#修改时间
    views = models.PositiveIntegerField(default = 0)#浏览量
    topped = models.BooleanField(default = False)#是否置顶
    likes = models.PositiveIntegerField(default = 0)#点赞数
    art_category = models.ForeignKey('Category')

    def __str__(self):
        return self.title
