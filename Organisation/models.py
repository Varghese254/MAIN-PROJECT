from django.db import models
from Guest.models import *
from Organisation import *
from User.models import *




class ScheduleShow(models.Model):
    schedule_title=models.CharField(max_length=50,null=True)
    organisation=models.ForeignKey(Organization,on_delete=models.CASCADE)
    schedule_date=models.DateField()
    schedule_time=models.TimeField()
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    schedule_venue=models.CharField(max_length=50)
    schedule_details=models.TextField(null=True)
    schedule_poster=models.FileField(upload_to='OrgDocs/')
    schedule_status=models.IntegerField(default=0)

class AddJudge(models.Model) :
     organisation=models.ForeignKey(Organization,on_delete=models.CASCADE)
     judge_name=models.CharField(max_length=50)
     judge_photo=models.FileField(upload_to='OrgDocs/')



# Create your models here.

class Result(models.Model):
   # schedule=models.ForeignKey(ScheduleShow,on_delete=models.SET_NULL,null=True)
    booking=models.ForeignKey("User.BookShow",on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0,null=True)

    result_position=models.CharField(max_length=50)

