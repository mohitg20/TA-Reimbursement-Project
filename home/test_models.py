from django.test import TestCase

from home.models import User_profile,Application

 
class TestAppModels(TestCase):
    
    def test_user_profile_str(self):
        user=User_profile.objects.create(user="profile")
        email=User_profile.objects.create(email="user@iitk.ac.in")
        name=User_profile.objects.create(name="NA")
        rollno=User_profile.objects.create(rollno="NA")
        designation=User_profile.objects.create(designation="NA")
        department=User_profile.objects.create(department="NA")
        bankname=User_profile.objects.create(bankname="NA")
        ACtype=User_profile.objects.create(ACtype="NA")
        AC=User_profile.objects.create(AC="NA")
        IFSC=User_profile.objects.create(IFSC="NA")
        aadhar=User_profile.objects.create(aadhar="NA")
        mobile=User_profile.objects.create(mobile="NA")
        # content=Post.objects.create(content="This is some content")
        self.assertEqual(str(email),"user@iitk.ac.in")
        
#     def test_application_str(self):
#         email=Application.objects.create(email="user@iitk.ac.in")
#         # content=Post.objects.create(content="This is some content")
#         self.assertEquals(str(email),"user@iitk.ac.in")



