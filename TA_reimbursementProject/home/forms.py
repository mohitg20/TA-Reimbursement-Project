from django.forms import ModelForm
from django.core.exceptions import ValidationError
# from .models import Order

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
# class ProfileForm(UserCreationForm):
#     class Meta:
#         model=home.models.User_profiles