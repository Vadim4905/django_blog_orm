from django.db import models

# Create your models here.

class Post(models.Model):
    name =  models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    
class Coment(models.Model):
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post,related_name='coments',on_delete=models.CASCADE)