from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils import timezone
from .signals import *

# Create your models here.
class CustomUser(User): #Derived from Django User
    '''
    id = models.IntegerField
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    is_superuser = models.BooleanField
    '''
    like_shop_num = models.CharField(max_length=128,default=0)
    image = models.ImageField(default=None)
    objects = UserManager()

class Shop(models.Model):
    #id = models.IntegerField()#(max_length=11)
    location = models.CharField(max_length=254)
    tel = models.CharField(max_length=128)
    time = models.CharField(max_length=254)
    name = models.CharField(max_length=128)
    price = models.IntegerField()#(max_length=11)
    area_id = models.CharField(max_length=254)
    type_id = models.CharField(max_length=254)
    comment_num = models.IntegerField()#(max_length=11)
    #score_num = models.IntegerField#(max_length=11)
    taste_score = models.FloatField()
    env_score = models.FloatField()
    serv_score = models.FloatField()
    rate = models.FloatField()
    image = models.CharField(max_length=254)
    addr = models.CharField(max_length=254)

class Accuse_user(models.Model):
    #id = models.IntegerField()#(max_length=11)
    accuser = models.ForeignKey(CustomUser, related_name='User_Accusers', related_query_name='User_Accuser')
    defendant = models.ForeignKey(CustomUser, related_name='User_Defendants', related_query_name='User_Defendant')
    content = models.TextField()

class Accuse_shop(models.Model):
    #id = models.IntegerField()#(max_length=11)
    accuser = models.ForeignKey(CustomUser, related_name='Shop_Accusers', related_query_name='Shop_Accuser')
    defendant = models.ForeignKey(Shop, related_name='Shop_Defendants', related_query_name='Shop_Defendant')
    content = models.TextField()

class New_shop(models.Model):
    #id = models.IntegerField()#(max_length=11)
    lcoation = models.CharField(max_length=254)
    tel = models.CharField(max_length=128)
    time = models.CharField(max_length=254)
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=None)#(max_length=11)
    area_id = models.IntegerField(default=None)#(max_length=11)
    type_id = models.IntegerField(default=None)#(max_length=11)
    rate = models.FloatField(default=None)
    # image = models.BinaryField todo
class Recommend(models.Model):
    #id = models.IntegerField()#(max_length=11)
    shop_id = models.ForeignKey(Shop, related_name='Shop_Recommends', related_query_name='Shop_Recommend')
    name = models.CharField(max_length=128)
    #pic = models.BinaryField todo

class Like_shop(models.Model):
    user_id = models.ForeignKey(CustomUser, related_name='CustomUser_Like_shops', related_query_name='CustomUser_Like_shop')
    shop_id = models.ForeignKey(Shop, related_name='Shop_Like_shops', related_query_name='Shop_Like_shop')

class Record(models.Model):
    user_id = models.ForeignKey(CustomUser, related_name='CustomUser_Records', related_query_name='CustomUser_Record')
    shop_id = models.ForeignKey(Shop, related_name='Shop_Records', related_query_name='Shop_Record')
    create_at = models.DateField(default=timezone.now)

class Comment(models.Model):
    user_id = models.ForeignKey(CustomUser, related_name='CustomUser_Comments', related_query_name='CustomUser_Comment')
    shop_id = models.ForeignKey(Shop, related_name='Shop_Comments', related_query_name='Shop_Comment')
    taste_score = models.IntegerField(default=0)
    env_score = models.IntegerField(default=0)
    serv_score = models.IntegerField(default=0)
    like_num = models.IntegerField(default=0)
    content = models.TextField()
    create_at = models.DateField(default=timezone.now)
