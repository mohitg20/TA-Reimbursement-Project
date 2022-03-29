import email
from pickle import GET
from xml.etree.ElementTree import tostring
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from home.models import *
from unicodedata import category
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#For Reset Password
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import *
# from .filters import OrderFilter

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return redirect('/home')
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
            messages.success(request,"Login successful!")
            if user.groups.filter(name="Office"):
                # print("Here 1")
                return render(request,"adminOffice.html",context={'user':user})
            elif user.groups.filter(name="Accounts"):
                return render(request,"accountOffice.html",context={'user':user})
            else:    
                # print("Here 2")
                return render(request,"home.html",context={'user':user})
            # A backend authenticated the credentials
        else:
            messages.warning(request,"Incorrect Credentials")
            return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required
def home(request):
    context={
        'user':request.user
    }
    return render(request,'home.html',context)    
    
@login_required
def status(request):
    dt=claimBill.objects.filter(email=request.user.email)
    dt2=Application.objects.filter(email=request.user.email)
    for d in [dt,dt2]:
        for fr in d:
            if fr.status==Application.ACCEPTED:
                fr.status=True
            elif fr.status==Application.REJECTED:
                fr.status=False
            else:
                fr.status=None
    context={
        'user':request.user,
        'claim' : dt,
        'application' : dt2
    }
    # print(request.user.email,dt[0].purpose)
    return render(request,'status.html',context)    

@login_required
def form(request):
    fr=claimBillForm()
    filled={}
    filled['email']=request.user.email
    filled['name']=request.user.profile.name
    filled['roll_number']=request.user.profile.rollno
    filled['designation']=request.user.profile.designation
    filled['department']=request.user.profile.department
    # filled['purpose']
    s=True
    level=1
    d=Application.objects
    if request.method=="POST":
        # print(str(request))
        fr=claimBillForm(request.POST)
        if fr.is_valid():
            t=fr.save(commit=False)
            t.email=request.user.email
            t.apl=d.get(email=request.user.email,pk=request.POST.__getitem__("application_pk"))
            t.roll_number=request.user.profile.rollno
            t.name=request.user.profile.name
            t.designation=request.user.profile.designation
            t.department=request.user.profile.department
            t.purpose=(t.apl).Purpose
            t.save()
            messages.success(request,"Request has been submitted successfully!")
            messages.info(request,"Please note your application id for future reference  :  "+str(t.pk))
        else:
            print(fr.errors)
            for value in fr.errors.values():
                messages.info(request,value)
    elif request.method=="GET":
        if request.GET.__contains__("application_pk"):
            if d.filter(email=request.user.email,pk=request.GET.__getitem__("application_pk")).count()==0:
                messages.warning(request,"Application not found")
            elif d.get(email=request.user.email,pk=request.GET.__getitem__("application_pk")).status!=Application.ACCEPTED:
                messages.warning(request,"Application is not yet accepted")
            else:
                filled['application_pk2']=request.GET.__getitem__("application_pk")
                filled['purpose']=d.get(pk=request.GET.__getitem__("application_pk")).Purpose
                level=2
        elif request.GET.__contains__("pk"):
            c=claimBill.objects
            if c.filter(email=request.user.email,pk=request.GET.__getitem__("pk")).count()==0:
                messages.warning(request,"Bill not found")
            else:
                level=2
                filled=c.get(email=request.user.email,pk=request.GET.__getitem__("pk")).__dict__
                s=False
    context={'fill_form':filled,'submit':s,'level':level}
    return render(request,'form.html',context)
def registerUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created successfully!")
            return render(request,"login.html")
        else :
            for value in form.errors.values():
                messages.info(request,value)
    context = {'form':form}
    return render(request,'register.html',context)

@login_required
def user_profile(request):
    fr=ProfileForm()
    filled={}
    filled['email']=request.user.email
    s=True
    if request.method=="POST":
        if request.user.profile.email:
            messages.info(request,"Profile already exists!")
            filled=request.user.profile.__dict__
            s=False
        else:
            fr=ProfileForm(request.POST,instance=request.user.profile)
            if fr.is_valid():
                t=fr.save(commit=False)
                t.email=request.user.email
                t.user=request.user
                t.save()
                messages.success(request,"Profile created successfully!")
                return redirect('/user_profile')
            else:
                print(fr.errors)
                for value in fr.errors.values():
                    messages.info(request,value)
    elif request.method=="GET":
        if request.user.profile.email:
            filled=request.user.profile.__dict__
            # print(filled)
            s=False
    context={'fill_form':filled,'submit':s}
    return render(request,'profile.html',context)

@login_required
def application(request):
    fr=ApplicationForm()
    filled={}
    filled['email']=request.user.email
    filled['profile']=request.user.profile
    filled['rollno']=request.user.profile.rollno
    filled['Name']=request.user.profile.name
    filled['section']=request.user.profile.department
    s=True
    admin=False
    if request.method=="POST":
        fr=ApplicationForm(request.POST)
        if fr.is_valid():
            t=fr.save(commit=False)
            t.email=request.user.email
            t.profile=request.user.profile
            t.rollno=request.user.profile.rollno
            t.Name=request.user.profile.name
            t.section=request.user.profile.department
            t.save()
            messages.success(request,"Request has been submitted successfully!")
            messages.info(request,"Please note your application id for future reference  :  "+str(t.pk))
        else:
            print(fr.errors)
            for value in fr.errors.values():
                messages.info(request,value)
    elif request.method=="GET":
        d=Application.objects
        if request.GET.__contains__("pk"):
            s=False
            if request.user.groups.filter(name="Office"):
                filled=d.get(pk=request.GET.__getitem__("pk")).__dict__
                admin=True
            elif d.filter(email=request.user.email,pk=request.GET.__getitem__("pk")).count()>0:
                filled=d.get(email=request.user.email,pk=request.GET.__getitem__("pk")).__dict__
                s=False
            # print(filled)
        else:
            if not request.user.profile.email:
                messages.error(request,"Update your Profile first")
                return redirect('/user_profile')
    context={'fill_form':filled,'submit':s,"admin":admin}
    return render(request,'application.html',context)

def redirecting(request):
    return redirect("/pending")

@login_required
def pending_requests(request):
    if request.user.groups.filter(name="Office"):
        d=Application.objects
        if request.method=="POST":
            if request.user.groups.filter(name="Office"):
                req=request.POST.dict()
                t=d.get(pk=req["id"])  
                if req["accept"]=='yes':
                    t.status=Application.ACCEPTED
                    messages.success(request,"Application accepted!")
                    # print(Application.objects.get(id=req['id']).status)
                    t.save()
                # elif req["accept"]=='viewapplication':
                #     # print(request.method)
                #     # request.method="hmmm"
                #     # print(request.method)
                #     # # return redirect("/application_form?pk="+req["id"])
                #     # if request.method=="POST2":
                #     #     return redirect("/pending")
                #     return render(request,"application.html",context={'pk':req["id"]})
                elif req["accept"]=='no':
                    t.status=Application.REJECTED
                    t.save()
                    messages.warning(request,"Application declined!")
            else:
                messages.warning(request,"You are not allowed for this request")
                return redirect("/home")
        return render(request,'pending.html',context={'Applications':d.filter(status=Application.PENDING)})
    elif request.user.groups.filter(name="Accounts"):
        d=claimBill.objects
        if request.method=="POST":
            if request.user.groups.filter(name="Accounts"):
                req=request.POST.dict()
                t=d.get(pk=req["id"])  
                if req["accept"]=='yes':
                    t.status=claimBill.ACCEPTED
                    messages.success(request,"Application accepted!")
                    # print(Application.objects.get(id=req['id']).status)
                    t.save()
                elif req["accept"]=='viewapplication':
                    request.method="hmmm"#Dont remove this line
                    if request.method=="POST2":
                        return redirect("/pending")
                    return render(request,"viewForm.html",context={'app':t})
                elif req["accept"]=='no':
                    t.status=claimBill.REJECTED
                    t.save()
                    messages.warning(request,"Application declined!")
            else:
                messages.warning(request,"You are not allowed for this request")
                return redirect("/home")
        return render(request,'pending.html',context={'Applications':d.filter(status=claimBill.PENDING)})
    
    else:
        messages.warning(request,"You are not allowed for this request")
        return redirect("/home")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')