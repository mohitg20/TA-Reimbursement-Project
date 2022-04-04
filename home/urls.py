from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index, name="home" ),
    path('login',views.loginUser, name="login" ),
    path('logout',views.logoutUser, name="logout" ),
    path('register',views.registerUser, name="register" ),
    path('user_profile',views.user_profile, name="user_profile" ),
    path('form',views.form, name="form" ),
    path('home',views.home, name="home" ),
    path('application_status',views.status, name="application_status" ),
    path('application_form',views.application, name="application_form" ),
    path('pending',views.pending_requests, name="pending"),
    # add forget password

]