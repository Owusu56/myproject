from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="ProductImages/")
    quantity = models.IntegerField()
    code = models.CharField(max_length=10)
    price = models.FloatField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name