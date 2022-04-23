# from attr import fields
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data
class ProfileForm(forms.ModelForm):
    class Meta:
        model=User_profile
        exclude=['email','user']
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude=['status','email','profile']

class claimBillForm(forms.ModelForm):
    
    class Meta:
        model = claimBill
        exclude=['apl','status','name','email','roll_number','designation','department','purpose']