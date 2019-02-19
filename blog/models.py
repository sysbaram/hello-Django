from django.conf import settings
from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     tags = models.CharField(max_length = 20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
   author = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
   title = models.CharField(max_length=100, db_index=True)
   content = models.TextField()
   tags = models.CharField(max_length=20)
   is_publish = models.BooleanField(default=False) #공개여부 default값을 줬으므로 아까와 같이 물어보지 않고 그냥 blank같은 설정값 디폴트
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   #post의 title을 post_object가 아니라, 실제 post의 tite을 보여주게 된다.
   def __str__(self):
       return self.title



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    auth_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   