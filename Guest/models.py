from django.db import models
from Admin.models import *
class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)

    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    user_pincode=models.CharField(max_length=50,null=True)

    user_photo=models.FileField(upload_to='UserDocs/')
    user_proof=models.FileField(upload_to='UserDocs/')
    user_password=models.CharField(max_length=50)
    dog_licence=models.CharField(max_length=50)
    dog_name=models.CharField(max_length=50,null=True)
    dog_breed=models.CharField(max_length=50,null=True)
    dog_gender=models.CharField(max_length=50)
    dog_age=models.CharField(max_length=50,null=True)
    user_address=models.CharField(max_length=100)
    dog_photo=models.FileField(upload_to='UserDocs/',null=True)

class Organization(models.Model):
    org_name=models.CharField(max_length=50)
    org_contact=models.CharField(max_length=50)
    org_email=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    org_photo=models.FileField(upload_to='UserDocs/')
    org_proof=models.FileField(upload_to='UserDocs/')
    org_password=models.CharField(max_length=50)
    org_address=models.CharField(max_length=100)    
    org_vstatus=models.IntegerField(default=0)


class Admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)    


# Create your models here.
