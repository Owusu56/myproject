from django.urls import path
from . import views

from .views import ShowCheckOut, CheckOut

urlpatterns = [
    path("ShowCheckOut/", ShowCheckOut, name="ShowCheckOut"),
    path("CheckOut/", CheckOut, name="CheckOut"),
    path('Payment/', views.Payment, name="Payment"),
    path('Success/', views.Success, name="Success"),

]
