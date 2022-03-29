import email
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
            messages.success(request,"Login sucessfull!")
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

# def pending(request):
#     return render(request,'pending.html')    
@login_required
def status(request):
    dt=claimBill.objects.filter(email=request.user.email)
    dt2=Application.objects.filter(email=request.user.email)
    for d in [dt,dt2]:
        for fr in d:
            if fr.status==1:
                fr.status=True
            elif fr.status==0:
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
    if request.method =="POST":
        institute=request.POST.get('institute')
        email=request.user.email
        project_number=request.POST.get('project_number')
        name=request.POST.get('name')
        roll_number=request.POST.get('roll_number')
        designation=request.POST.get('designation')
        department=request.POST.get('department')
        pay_band=request.POST.get('pay_band')
        purpose=request.POST.get('purpose')
        travel_cost=request.POST.get('travel_cost')
        road_kms=request.POST.get('road_kms')
        hospitality_availed=request.POST.get('hospitality_availed')
        hospitality_not_availed=request.POST.get('hospitality_not_availed')
        expenses=request.POST.get('expenses')
        total=request.POST.get('total')
        less_advance=request.POST.get('less_advance')
        net=request.POST.get('net')
        drivelink=request.POST.get('drivelink')

        name1=request.POST.get('name1')
        name2=request.POST.get('name2')
        name3=request.POST.get('name3')
        name4=request.POST.get('name4')
        name5=request.POST.get('name5')
        
        date1=request.POST.get('date1')
        date2=request.POST.get('date2')
        date3=request.POST.get('date3')
        date4=request.POST.get('date4')
        date5=request.POST.get('date5')
        
        age1=request.POST.get('age1')
        age2=request.POST.get('age2')
        age3=request.POST.get('age3')
        age4=request.POST.get('age4')
        age5=request.POST.get('age5')
        
        rel1=request.POST.get('rel1')
        rel2=request.POST.get('rel2')
        rel3=request.POST.get('rel3')
        rel4=request.POST.get('rel4')
        rel5=request.POST.get('rel5')
        
        part1=request.POST.get('part1')
        part2=request.POST.get('part2')
        part3=request.POST.get('part3')
        part4=request.POST.get('part4')
        part5=request.POST.get('part5')
        
        amt1=request.POST.get('amt1')
        amt2=request.POST.get('amt2')
        amt3=request.POST.get('amt3')
        amt4=request.POST.get('amt4')
        amt5=request.POST.get('amt5')
        
        
        # email=request.POST.get('email')
        form=claimBill(drivelink=drivelink,institute=institute,email=email,project_number=project_number,name=name ,roll_number=roll_number,designation=designation,department=department,pay_band=pay_band,purpose=purpose,travel_cost=travel_cost,road_kms=road_kms,hospitality_availed=hospitality_availed,hospitality_not_availed=hospitality_not_availed,expenses=expenses,total=total,less_advance=less_advance,net=net,name1=name1,name2=name2,name3=name3,name4=name4,name5=name5,date1=date1,date2=date2,date3=date3,date4=date4,date5=date5,age1=age1,age2=age2,age3=age3,age4=age4,age5=age5,rel1=rel1,rel2=rel2,rel3=rel3,rel4=rel4,rel5=rel5,part1=part1,part2=part2,part3=part3,part4=part4,part5=part5,amt1=amt1,amt2=amt2,amt3=amt3,amt4=amt4,amt5=amt5)
        form.save()
    if(claimBill.objects.filter(email=request.user.email).exists()):
        plz = claimBill.objects.get(email=request.user.email)
        return render(request,'filledform.html',context={'username':plz})
    else:
        if User_profile.objects.filter(email=request.user.email).exists():
            plz=User_profile.objects.get(email=request.user.email)
            # print(plz.email)
            return render(request,'form.html',context={'username':plz})
        else:
            return render(request,'formBase.html',context={'userdata':request.user})
        # return render(request,'status.html')
    # return render(request,'form.html')    
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
    if request.method=="POST":
        # print(str(request))
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
        if request.GET.__contains__("pk"):
            s=False
            filled=Application.objects.filter(email=request.user.email,pk=request.GET.__getitem__("pk"))[0].__dict__
            # print(filled)
        elif not request.user.profile.email:
            messages.error(request,"Update your Profile first")
            return redirect('/user_profile')
    context={'fill_form':filled,'submit':s}
    return render(request,'application.html',context)
# def pending_requests(request):

#     plz=Application.objects.get(email="user@iitk.ac.in")
#     print(plz.email)
#     # return render(request,'pending.html',{'AppData':plz})
#     if User_profile.objects.filter(email=request.user.email).exists():
#         plz=User_profile.objects.get(email=request.user.email)
#         # print(plz.email)
#         return render(request,'application.html',context={'username':plz})
#     else:
#         return render(request,'applicationBase.html',context={'username':request.user})
#     return render(request,'application.html')

@login_required
def pending_requests(request):
    d=Application.objects
    if request.method=="POST":
        if request.user.groups.filter(name="Office"):
            req=request.POST.dict()
            t=d.get(id=req["id"])
            # print(request.POST)
            if req["accept"]=='yes':
                t.status=Application.ACCEPTED
                messages.success(request,"Application accepted!")
                # print(Application.objects.get(id=req['id']).status)
                t.save()
            else:
                t.status=Application.REJECTED
                messages.warning(request,"Application declined!")
        else:
            messages.warning(request,"You are not allowed for this request")
            redirect("/home")
    return render(request,'pending.html',context={'AppData':d.filter(status=Application.ACCEPTED)})
    


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')