from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Reader(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    #photo = models.ImageField(upload_to="images/swapper_photos/")

    def __unicode__(self):
        return self.name


class News(models.Model):
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    click = models.IntegerField(max_length=10000)
    genre = models.CharField(max_length=100)
    topic=models.CharField(max_length=500)



class Clicks(models.Model):
    user_id=models.CharField(max_length=100)
    news_id=models.CharField(max_length=100)
    date=models.DateField()


class RecedNews(models.Model):
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    value=models.CharField(max_length=500)
    genre=models.CharField(max_length=500)

