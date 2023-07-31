from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from django.core.mail import send_mail 
from django.conf import settings 
import random
def reg(request):
    dis=District.objects.all()
    pl=Place.objects.all()  
    if request.method=="POST":  
        p=Place.objects.get(id=request.POST.get('place'))

        d=User.objects.filter(user_email=request.POST.get("email"))
        if d:
            return render(request,"Guest\Registration.html",{'msg':"Email already exists"})
        else: 

         User.objects.create(user_name=request.POST.get('txtname'),user_pincode=request.POST.get('txtpin'),user_contact=request.POST.get('contact'),user_email=request.POST.get('email'),place=p,user_photo=request.FILES.get('photo'),user_proof=request.FILES.get('proof'),user_password=request.POST.get('password'),dog_licence=request.POST.get('dogno'),user_address=request.POST.get('txtad'),dog_name=request.POST.get('txt_dname'),dog_breed=request.POST.get('txt_breed'),dog_gender=request.POST.get('gender'),dog_age=request.POST.get('txt_age'),dog_photo=request.FILES.get('dogphoto'))
        request.session["femail"]=request.POST.get('email') 
        send_mail( 
            'Respected Sir/Madam.',#subject 
            "Successfully Registered in TalentDogs,Now You Can Login With Your Given Email_ID And Password.Thank You,Have A Nice Day.",#body 
            settings.EMAIL_HOST_USER, 
            [request.POST.get('email')], 
        ) 
    
        return render(request,"Guest\Registration.html",{'msg':"Registered Successfully"})
    else:
      return render(request,"Guest\Registration.html",{'dis':dis,'pl':pl}) 

def oreg(request):
    dis=District.objects.all()
    pl=Place.objects.all()  
    if request.method=="POST":  
        p=Place.objects.get(id=request.POST.get('place'))

        d=Organization.objects.filter(org_email=request.POST.get("email"))
        if d:
            return render(request,"Guest\Registration.html",{'msg':"Email already exists"})
        else: 

         Organization.objects.create(org_name=request.POST.get('txtname'),org_contact=request.POST.get('contact'),org_email=request.POST.get('email'),place=p,org_photo=request.FILES.get('photo'),org_proof=request.FILES.get('proof'),org_password=request.POST.get('password'),org_address=request.POST.get('txtad'),org_vstatus='0')
        return render(request,"Guest\OrganizationReg.html",{'msg':"Registered Successfully"})
    else:
      return render(request,"Guest\OrganizationReg.html",{'dis':dis,'pl':pl})    


    

def Login(request): 
    if request.method=="POST":  
        organizationcount=Organization.objects.filter(org_email=request.POST.get('email'),org_password=request.POST.get('password'),org_vstatus=1).count()
        usercount=User.objects.filter(user_email=request.POST.get('email'),user_password=request.POST.get('password')).count() 
        admincount=Admin.objects.filter(admin_email=request.POST.get('email'),admin_password=request.POST.get('password')).count()   
        if organizationcount > 0:
            organization=Organization.objects.get(org_email=request.POST.get('email'),org_password=request.POST.get('password'),org_vstatus=1)
            request.session['oid']=organization.id
            request.session['oname']=organization.org_name
            return redirect('weborganisation:Home')
        elif usercount > 0:
            user=User.objects.get(user_email=request.POST.get('email'),user_password=request.POST.get('password'))  
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('webuser:Home')

        elif admincount > 0:
            admin=Admin.objects.get(admin_email=request.POST.get('email'),admin_password=request.POST.get('password'))  
            request.session['aid']=admin.id
            request.session['aname']=admin.admin_name
            return redirect('webadmin:Home')
        else:
            return render(request,'Guest/Login.html') 
              
    else:
        return render(request,'Guest/Login.html')    

def ForgotPass(request): 
    if request.method=="POST": 
        otp=(random.randint(100000,999999)) 
        request.session["otp"]=otp 
        request.session["femail"]=request.POST.get('txt_email') 
        send_mail( 
            'Respected Sir/Madam '+" ",#subject 
            "Your Otp is"+str(otp),#body 
            settings.EMAIL_HOST_USER, 
            [request.POST.get('txt_email')], 
        ) 
        return redirect('webguest:validateotp') 
    else: 
        return render(request,"Guest/ForgotPassword.html")

def ValidateOtp(request): 
    if request.method=="POST": 
        otp=request.POST.get("txt_otp") 
        ce=str(request.session["otp"]) 
        if otp==ce: 
            return redirect("webguest:createpass") 
    return render(request,"Guest/ValidateOTP.html") 

def CreatePass(request): 
    if request.method=="POST": 
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"): 
            usercount=User.objects.filter(user_email=request.session["femail"]).count() 
            organizationcount=Organization.objects.filter(org_email=request.session["femail"]).count() 
            if usercount>0: 
                user=User.objects.get(user_email=request.session["femail"]) 
                user.user_password=request.POST.get("txt_pass") 
                user.save() 
                return redirect("webguest:login") 
            elif organizationcount>0: 
                  technician=Organization.objects.get(org_email=request.session["femail"]) 
                  technician.org_password=request.POST.get("txt_pass") 
                  technician.save() 
                  return redirect("webguest:login") 
        else: 
            return render(request,"Guest/CreatePassword.html",{'msg':"Passwords not same"}) 
    else: 
        return render(request,"Guest/CreatePassword.html")           




# Create your views here.
