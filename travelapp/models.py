from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics')

class Blog(models.Model):
    image = models.ImageField(upload_to='blogs')
    day = models.IntegerField()
    month = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    desc = models.TextField()


