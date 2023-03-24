from django.db import models

# Create your models here.

models_list = ['title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description', 'actor_image']

class Article(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField()
