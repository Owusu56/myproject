from django.shortcuts import render
from .models import Product

# # Create your views here.
# from itertools import count

# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# # Create your views here.
# from django.views.generic import ListView, DetailView
# from .models import Product, ProductImage, ProductInfo
# from cart.models import Cart


# class ProductList(ListView):
#     model = Product
#     template_name = "product/shop.html"
#     context_object_name = "product"


# class ProductDetail(DetailView):
#     model = Product
#     template_name = "product/show.html"
#     context_object_name = "product"


# def productDetail2(request, product_id):
#     product = Product.objects.get(id=product_id)
#     imageModel = ""
#     product_info = ""

#     if ProductImage.objects.filter(product=product).count():
#         imageModel = ProductImage.objects.filter(product=product).get()

#     if ProductInfo.objects.filter(product=product).count():
#         product_info = ProductImage.objects.filter(product=product).get()

#     relatedProduct = Product.objects.raw('SELECT * FROM product_product WHERE  name  LIKE  %s limit 2', [product.name])

#     # relatedProduct = Product.objects.filter(name=product.name)
#     for pro in relatedProduct:
#         print(pro)
#     context = {"def_product": product, "imagelist": imageModel, 'related': relatedProduct, 'product_info': product_info}
#     return render(request, "product/show.html", context)


# def Home(request):
#     phones = Product.objects.filter(name="phone")
#     laptop = Product.objects.filter(name="laptop")
#     Tv = Product.objects.filter(name="Tv")
#     context = {"Phone": phones, "Laptop": laptop, "Tv": Tv}

#     if request.user.is_authenticated:
#         Added_cart = Cart.objects.filter(user=request.user).count()
#         request.session['cart'] = Added_cart
#         request.session.modified = True
#         return render(request, "product/home.html", context)
#     else:

#         request.session['cart'] = 0
#         return render(request, "product/home.html", context)

def product_list(request):
    phones = Product.objects.all()
    return render(request, "product/product_list.html", {'phone': phones})
