from django.conf import settings
from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     tags = models.CharField(max_length = 20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Shop(models.Model):
#   author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   desc = models.TextField(blank=True)
   address = models.CharField(max_length=50, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   #post의 title을 post_object가 아니라, 실제 post의 tite을 보여주게 된다.
   def __str__(self):
       return self.name



class Item(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
