from django.test import TestCase

from home.models import User_profile,Application
from django.contrib.auth.models import User
 
class TestAppModels(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('foo','user@iitk.ac.in','qwer@123')
        
    def test_user_profile_str(self):
        self.assertEqual(self.user.email,"user@iitk.ac.in")
        self.assertEqual(self.user.profile.email,"user@iitk.ac.in")
        
#     def test_application_str(self):
#         email=Application.objects.create(email="user@iitk.ac.in")
#         # content=Post.objects.create(content="This is some content")
#         self.assertEquals(str(email),"user@iitk.ac.in")



