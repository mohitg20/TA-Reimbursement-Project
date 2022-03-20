from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from home.models import Form
from unicodedata import category
from home.models import User_profile
from django.contrib import messages

from .forms import CreateUserForm
# from .filters import OrderFilter

from django.contrib.auth.forms import UserCreationForm


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
            return redirect("/home")
            # A backend authenticated the credentials
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')

def home(request):
    return render(request,'home.html')    



def form(request):
    if request.method =="POST":
        institute=request.POST.get('institute')
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
        form=Form(institute=institute,project_number=project_number,name=name ,roll_number=roll_number,designation=designation,department=department,pay_band=pay_band,purpose=purpose,travel_cost=travel_cost,road_kms=road_kms,hospitality_availed=hospitality_availed,hospitality_not_availed=hospitality_not_availed,expenses=expenses,total=total,less_advance=less_advance,net=net,name1=name1,name2=name2,name3=name3,name4=name4,name5=name5,date1=date1,date2=date2,date3=date3,date4=date4,date5=date5,age1=age1,age2=age2,age3=age3,age4=age4,age5=age5,rel1=rel1,rel2=rel2,rel3=rel3,rel4=rel4,rel5=rel5,part1=part1,part2=part2,part3=part3,part4=part4,part5=part5,amt1=amt1,amt2=amt2,amt3=amt3,amt4=amt4,amt5=amt5)
        form.save()
    return render(request,'form.html')    

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
                messages.error(request,value)
            
    context = {'form':form}
    return render(request,'register1.html',context)
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        
        return redirect('/login')
    

def user_profile(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        rollno=request.POST.get('rollno')
        designation=request.POST.get('designation')
        department=request.POST.get('department')
        bankname=request.POST.get('bankname')
        ACtype=request.POST.get('ACtype')
        AC=request.POST.get('AC')
        IFSC=request.POST.get('IFSC')
        aadhar=request.POST.get('aadhar')
        mobile=request.POST.get('mobile')
        user=User_profile(name=name, email=email, rollno=rollno, designation=designation,department=department,bankname=bankname,ACtype=ACtype,AC=AC,IFSC=IFSC,aadhar=aadhar,mobile=mobile)
        user.save()
    return render(request,'user_profile.html')


