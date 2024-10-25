from django.db import models
from django.contrib.auth.models import User



# Create your models here.
# class Thread(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add= True)




class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.body



class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.message



# class Thread(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
