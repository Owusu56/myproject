from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from custom_user.admin import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.core.mail import send_mail
from verify_email import send_verification_email

# Create your views here.
inactive_user = ''

def index(request):
    context = {"key": "I am at Home "}
    return render(request, "authentication/home.html", context)


class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.method == "POST":
            try:
                remember_me = str(self.request.POST['checkbox'])
                if remember_me: 
             # This if statement can change, 
             # but the purpose is checking remember me checkbox is checked or not.
                   self.request.session.set_expiry(86400 * 28) # Here we extend session.
                   print("Check")

            except:
                   # This part of code means, close session when browser is closed.
                   self.request.session.set_expiry(0) 
                   print("UnCheck")


        else:
             # GET method
             if self.request.user.is_authenticated: 
                print(" Remember ME !!!!")
        return reverse_lazy('home')
        

def send_welcome_email(request):
        subject = 'Welcome To My Site'
        massage = 'Thank you for creating an account!'
        from_mail = 'admin@Mysite.com'
        global inactive_user
        recepient_list = [inactive_user]
        send_mail(subject,massage,from_mail,recepient_list)
        return redirect("home")

class CustomRegisterView(FormView):
    template_name = "authentication/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home") # Automatically redirect to homepage after Registration

    def form_valid(self, form):
        # user = form.save()  # Automatically Save Registering User
        global inactive_user
        inactive_user = send_verification_email(self.request, form) 
        form.cleaned_data['email']
        if inactive_user is not None:
            login(self.request, inactive_user)  # Automatically log us in
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")  # Prevent User Registeration form from showing
        return super(CustomRegisterView, self).get(request, *args, **kwargs)
    



    
    
