from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image




class Post1(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='movies/')
    movie_director = models.CharField(max_length=40)
    movie_actor = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.title}{self.content}{self.date_posted}{self.author}{self.image} {self.movie_director} {self.movie_actor}"

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Post2(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='movies/')
    movie_director = models.CharField(max_length=40)
    movie_actor = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.title}{self.content}{self.date_posted}{self.author}{self.image} {self.movie_director} {self.movie_actor}"

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


