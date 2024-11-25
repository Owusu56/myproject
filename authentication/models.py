from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=225, null=True)
    price = models.FloatField()
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self) -> str:
        return self.title + ' ' + self.body
    
title = models.CharField(max_length=12)
image = models.ImageField(null=True,blank=True,upload_to="images/")