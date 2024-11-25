from django.shortcuts import render


import random
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from cart.models import Cart
# Create your views here.
from .models import Checkout
from .forms import CheckoutForm
from product.models import Product

def Payment(request):
    return render(request, 'checkouts/payment.html')

def Success(request):
    return render(request, 'checkouts/success.html')


def ShowCheckOut(request):
    if request.user.is_authenticated:

        cart = Cart.objects.filter(user=request.user)
        prod = []
        car = []
        for Data in cart:
            print(Data.product)
            products = Product.objects.filter(name=Data.product)
            for productData in products:
                prod.append(productData.code)
            car.append(Data.quantity)
        print(prod)



        form = CheckoutForm
        # MyQuantityRange = ""

        total = sum(item.Total_cost() for item in cart)

        # for cartdat in cart:
        #     MyQuantityRange = range(cartdat.product.quantity)
        # print(MyQuantityRange)
        
        print(str(random.randint(200,757)))
       

                                             
        if request.method == "POST":
            form = CheckoutForm(request.POST)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.product = prod
                newform.cart = car
                newform.user = request.user
                newform.door_to_door_fee = 40.5
                newform.shipping = 40.5
                newform.price = total + 40.5 + 40.5
                newform.customer_code = str(request.user) + str(random.randint(200007647,7577880058))
                newform.save()   
            else:
               form = CheckoutForm()
    
        context = {"cart": cart, "total": total, "form":form}
        return render(request, "checkouts/checkout.html", context)

    return render(request, "checkouts/checkout.html", {})


def CheckOut(request):
    if request.user.is_authenticated:
        if request.method == "POST":
           
           
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # surname = request.POST['surname']
            # user = request.user
            
            # customer_code = str(request.user) + str(random.randint(200007647,7577880058))
            # email = request.POST['email']
            # address = request.POST['address']
            # shipping = 100.55
            # door_to_door_fee = 100.74
            # price =  shipping + door_to_door_fee +1000

            # myDATA = Checkout(
            #       first_name = first_name, 
            #       last_name = last_name,
            #       surname = surname,
            #       user = user,
            #       customer_code =customer_code,
            #       email=email,
            #       address=address,
            #       shipping = shipping,
            #        door_to_door_fee= door_to_door_fee,
            #        price = price
            #                   )
            # myDATA.save()
            # form = CheckoutForm(request.POST)
            # form.save()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 
              
   
