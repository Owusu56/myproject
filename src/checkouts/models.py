from custom_user.models import User
from django.db import models

# Create your models here.

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=250)
    product = models.CharField(max_length=4000, null=True)
    cart = models.CharField(max_length=5000, null=True)
    email = models.EmailField(max_length=250)
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    shipping = models.FloatField()
    door_to_door_fee = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

  

    
   
       