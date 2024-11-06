from custom_user.models import User
from django.db import models

# Create your models here.
from django.http import request
from product.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name) + " ----- " + str(self.quantity)

    def Total_cost(self):
        return self.quantity * self.product.price

    def Twelve(self):

        if request.POST['mode'] <= 12:
            return request.POST['mode']

    def Thirty(self):

        if request.POST['mode'] <= 30:
            return request.POST['mode']

