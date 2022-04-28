from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import index,loginUser,logoutUser,registerUser,user_profile,form,home,status,pending_requests,application

class TesUrls(SimpleTestCase):
    
    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
        
    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, loginUser)
        
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logoutUser)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerUser)
        
    def test_user_profile_url_is_resolved(self):
        url = reverse('user_profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_profile)
        
    def test_form_url_is_resolved(self):
        url = reverse('form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, form)
        
    def test_index_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
        
    def test_status_url_is_resolved(self):
        url = reverse('application_status')
        print(resolve(url))
        self.assertEquals(resolve(url).func, status)
        
    def test_application_url_is_resolved(self):
        url = reverse('application_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, application)
        
    def test_pending_url_is_resolved(self):
        url = reverse('pending')
        print(resolve(url))
        self.assertEquals(resolve(url).func, pending_requests)