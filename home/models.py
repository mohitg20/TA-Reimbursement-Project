from email.mime import application
from django.db import models
from email.policy import default
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# class Task(models.Model):
#     REJECTED = 0
#     PENDING = -1
#     ACCEPTED = 1

#     Status = (
#         (REJECTED, 'Cancelled'),
#         (PENDING, 'Pending for admin approval'),
#         (ACCEPTED, 'Request accepted'),
#     )

#     status = models.IntegerField(choices=Status, default=PENDING)
#     def __str__(self):
#         return self.Status[self.status][1]
    
class User_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    rollno = models.CharField(max_length=10)
    designation = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    bankname = models.CharField(max_length=30)
    ACtype = models.CharField(max_length=10)
    AC = models.CharField(max_length=20)
    IFSC = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class Application(models.Model):
    profile=models.ForeignKey(User_profile,on_delete=models.CASCADE,related_name="applications")
    block_yr=models.CharField(default='' , max_length=122)
    email=models.EmailField(default='user@iitk.ac.in',max_length=30)
    rollno=models.CharField(default='' , max_length=122)
    basic_pay=models.CharField(default='' , max_length=122)
    Name=models.CharField(default='NA',max_length=122)
    Designation=models.CharField(default='NA',max_length=122)
    section=models.CharField(default='NA',max_length=122)
    avail=models.CharField(default='NA',max_length=122)
    duration=models.CharField(default='' , max_length=122)
    departure=models.CharField(default='' , max_length=122)
    nature=models.CharField(default='NA',max_length=122)
    Purpose=models.CharField(default='NA',max_length=122)
    place=models.CharField(default='NA',max_length=122)
    place1=models.CharField(default='NA',max_length=122)
    address=models.CharField(default='NA',max_length=122)
    mode=models.CharField(default='NA',max_length=122)
    Name1=models.CharField(default='NA',max_length=122)
    Age1=models.CharField(default='' , max_length=122)
    Name2=models.CharField(default='NA',max_length=122)
    Age2=models.CharField(default='' , max_length=122)
    Name3=models.CharField(default='NA',max_length=122)
    Age3=models.CharField(default='' , max_length=122)
    advance=models.CharField(default='' , max_length=122)
    REJECTED = 0
    PENDING = -1
    ACCEPTED = 1

    Status = (
        (REJECTED, 'Cancelled'),
        (PENDING, 'Pending for admin approval'),
        (ACCEPTED, 'Request accepted'),
    )

    status = models.IntegerField(choices=Status, default=PENDING)
    # def status_str(self):
    #     return self.Status[self.status][1]
    def __str__(self):
        return self.email

@receiver(post_save, sender=User_profile)
def save_user_profile(sender, instance, **kwargs):
    for apl in instance.applications.all():
        apl.profile=instance
class claimBill(models.Model):
    apl=models.OneToOneField(Application,on_delete=models.CASCADE,default=None,related_name="claimBill")
    # formid=models.IntegerField(default=-1)
    institute=models.CharField(max_length=122)
    email=models.EmailField(default='user@iitk.ac.in',max_length=30)
    project_number=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    roll_number=models.CharField(max_length=122)
    designation=models.CharField(max_length=122)
    department=models.CharField(max_length=122)
    pay_band=models.CharField(max_length=122)
    purpose=models.TextField()
    travel_cost=models.CharField( default='', max_length=122)
    road_kms=models.CharField( default='', max_length=122)
    hospitality_availed=models.CharField( default='', max_length=122)
    hospitality_not_availed=models.CharField( default='', max_length=122)
    expenses=models.CharField( default='', max_length=122)
    total=models.CharField( default='', max_length=122)
    less_advance=models.CharField( default='', max_length=122)
    net=models.CharField( default='', max_length=122)
    drivelink=models.CharField(default="NA",max_length=200)
    name1=models.CharField(default='NA', max_length=122)
    name2=models.CharField(default='NA', max_length=122)
    name3=models.CharField(default='NA', max_length=122)
    name4=models.CharField(default='NA', max_length=122)
    name5=models.CharField(default='NA', max_length=122)
    date1=models.CharField(default='NA', max_length=15)
    date2=models.CharField(default='NA', max_length=15)
    date3=models.CharField(default='NA', max_length=15)
    date4=models.CharField(default='NA', max_length=15)
    date5=models.CharField(default='NA', max_length=15)
    age1=models.CharField(default='' , max_length=122)
    age2=models.CharField(default='' , max_length=122)
    age3=models.CharField(default='' , max_length=122)
    age4=models.CharField(default='' , max_length=122)
    age5=models.CharField(default='' , max_length=122)
    rel1=models.CharField(default='NA',max_length=122)
    rel2=models.CharField(default='NA',max_length=122)
    rel3=models.CharField(default='NA',max_length=122)
    rel4=models.CharField(default='NA',max_length=122)
    rel5=models.CharField(default='NA',max_length=122)
    part1=models.CharField(default="NA",max_length=122)
    part2=models.CharField(default="NA",max_length=122)
    part3=models.CharField(default="NA",max_length=122)
    part4=models.CharField(default="NA",max_length=122)
    part5=models.CharField(default="NA",max_length=122)
    amt1=models.CharField(default='' , max_length=122)
    amt2=models.CharField(default='' , max_length=122)
    amt3=models.CharField(default='' , max_length=122)
    amt4=models.CharField(default='' , max_length=122)
    amt5=models.CharField(default='' , max_length=122)
    REJECTED = 0
    PENDING = -1
    ACCEPTED = 1

    Status = (
        (REJECTED, 'Cancelled'),
        (PENDING, 'Pending for admin approval'),
        (ACCEPTED, 'Request accepted'),
    )

    status = models.IntegerField(choices=Status, default=PENDING)
    # def __str__(self):
    #     return self.Status[self.status][1]
    def __str__(self):
        return self.email





