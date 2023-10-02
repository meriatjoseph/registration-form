from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required(login_url='login')
def HomePage(request):
    
    return render (request,'home.html')
    

def SignupPage(request):

    if request.method=="POST":
        uname=request.POST["username"]
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']


        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same!!!")
        
        else:
            pass

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

        print(uname,email,pass1,pass2)
    return render (request,'signup.html')

def LoginPage(request):
    
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass']
        user=authenticate(request, username=username,password=pass1,)
        if user is not None:
            
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')