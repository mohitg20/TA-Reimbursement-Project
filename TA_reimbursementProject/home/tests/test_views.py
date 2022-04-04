from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from home.models import User_profile,create_user_profile,save_user_profile,Application,save_user_profile,claimBill
import json

#class TestViews(TestCase): 
    
    # def test_index_GET(self): 
    #     client= Client()
    #     response=client.get(reverse('home'))
        
    #     self.assertEquals(response.status_code,302)
    #     self.assertTemplateUsed(response, 'home.html')
    
    # def test_loginUser_GET(self):
    #     client=Client()
    #     response=client.get(reverse('login'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'login.html')
        