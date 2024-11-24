from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import send_welcome_email
from  .views import CustomLoginView
from  .views import CustomRegisterView
from django.views.generic.base import RedirectView



urlpatterns = [
     path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
     path('send-welcome-mail/',send_welcome_email,name = 'send-welcome-mail'),
     path("login/",CustomLoginView.as_view(),name="login"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     path('accounts/login/',CustomLoginView.as_view(),name='login'),
     path('login/', RedirectView.as_view(url='accounts/login'),name="login"),

]

