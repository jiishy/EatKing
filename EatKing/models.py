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
    like_shop_num = models.CharField(max_length=128,default=None)
    image = models.ImageField
    objects = UserManager()
class Shop(models.Model):
    id = models.IntegerField#(max_length=11)
    lcoation = models.CharField(max_length=254)
    tel = models.CharField(max_length=128)
    time = models.CharField(max_length=254)
    name = models.CharField(max_length=128)
    price = models.IntegerField#(max_length=11)
    area_id = models.IntegerField#(max_length=11)
    type_id = models.IntegerField#(max_length=11)
    comment_num = models.IntegerField#(max_length=11)
    score_num = models.IntegerField#(max_length=11)
    taste_score = models.FloatField
    env_score = models.FloatField
    serv_score = models.FloatField
    rate = models.FloatField
    # image = models.BinaryField todo

class Recommend(models.Model):
    id = models.IntegerField#(max_length=11)
    shop_id = models.IntegerField#(max_length=11)
    name = models.CharField(max_length=128)
    #pic = models.BinaryField todo

class Like_shop(models.Model):
    id = models.IntegerField#(max_length=11)
    user_id = models.IntegerField#(max_length=11)
    shop_id = models.IntegerField#(max_length=11)

class Record(models.Model):
    id = models.IntegerField#(max_length=11)
    user_id = models.IntegerField#(max_length=11)
    shop_id = models.IntegerField#(max_length=11)
    create_at = models.DateField

class Comment(models.Model):
    id = models.IntegerField#(max_length=11)
    user_id = models.IntegerField#(max_length=11)
    shop_id = models.IntegerField#(max_length=11)
    taste_score = models.FloatField
    env_score = models.FloatField
    serv_score = models.FloatField
    like_num = models.IntegerField#(max_length=11)
    content = models.CharField(max_length=100)
    create_at = models.DateField

class Accuse_user(models.Model):
    id = models.IntegerField#(max_length=11)
    accuser = models.IntegerField#(max_length=11)
    defendant = models.IntegerField#(max_length=11)
    content = models.CharField(max_length=100)

class Accuse_shop(models.Model):
    id = models.IntegerField#(max_length=11)
    accuser = models.IntegerField#(max_length=11)
    defendant = models.IntegerField#(max_length=11)
    content = models.CharField(max_length=100)

class New_shop(models.Model):
    id = models.IntegerField#(max_length=11)
    lcoation = models.CharField(max_length=254)
    tel = models.CharField(max_length=128)
    time = models.CharField(max_length=254)
    name = models.CharField(max_length=128)
    price = models.IntegerField#(max_length=11)
    area_id = models.IntegerField#(max_length=11)
    type_id = models.IntegerField#(max_length=11)
    rate = models.FloatField
    # image = models.BinaryField todo