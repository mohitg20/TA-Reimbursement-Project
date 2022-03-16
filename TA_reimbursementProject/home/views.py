from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request,'index.html')
    else:
        # Do something for anonymous users.
        return redirect("/login")


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check user credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def registerUser(request):
    
    return render(request,'register.html')