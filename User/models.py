from django.db import models
from Admin.models import Product
from Guest.models import User,Organization
from Organisation.models import ScheduleShow
class Complaint(models.Model):
    organisation_name=models.ForeignKey(Organization,on_delete=models.CASCADE)     
    complaint_title=models.CharField(max_length=50)   
    complaint_details=models.TextField(null=True)  
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True) 
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)


class Feedback(models.Model):
    organisation_name=models.ForeignKey(Organization,on_delete=models.CASCADE)     
    feedback_content=models.CharField(max_length=50)   
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)    
    def __str__(self):
        return self.feedback_content

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    booking_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    cart_status=models.IntegerField(default=0)
    booking_date=models.DateField(auto_now=True,null=True)






class Cart(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    cart_qty=models.IntegerField(default=1)



class BookShow(models.Model):
    schedule=models.ForeignKey(ScheduleShow,on_delete=models.SET_NULL,null=True)
    booking_sts=models.IntegerField(default=0)
    payment_sts=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    booking_date=models.DateField(auto_now=True)
    result_sts=models.IntegerField(default=0,null=True)


   
class ProdBooking(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    booking=models.ForeignKey(Booking,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    booking_address=models.CharField(max_length=50) 
    booking_contact=models.CharField(max_length=50) 
    booking_pincode=models.CharField(max_length=50) 
    booking_amount=models.CharField(max_length=50)
    booking_date=models.DateField(auto_now=True,null=True)




class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=False, null=True, related_name="to_user")
    from_org = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, default=False, null=True, related_name="rom_org")
    to_org = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, default=False, null=True, related_name="to_org")
    content = models.TextField()
