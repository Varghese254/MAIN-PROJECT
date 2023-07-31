from django.shortcuts import render,redirect
from django.core.mail import send_mail 
from django.conf import settings 
import random

# Create your views here.
from Admin.models import *
from Guest.models import *
from User.models import *

def Home(request):
    admin=Admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/HomePage.html",{'data':admin})

def AdminProfile(request):
    pro=Admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/MyProfile.html",{'data':pro}) 


def EditProfile(request):
    pro=Admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        pro.admin_name=request.POST.get('txt_name')
        pro.admin_email=request.POST.get('txt_email')
        pro.save()
        return redirect("webadmin:edtpro")
    else:
        return render(request,"Admin/EditProfile.html",{'data':pro}) 

def Logout(request):
    return redirect('webguest:Login')            


def dis(request):
    dist = District.objects.all()
    if request.method=="POST":
      d=District.objects.filter(district_name=request.POST.get("District"))
      if d:
            return render(request,"Admin/District.html",{'res':dist,'msg':"Data already exists"})
      else: 

        District.objects.create(district_name=request.POST.get('District'))
        return render(request,"Admin\District.html",{'dis':dist,'msg':"Data Inserted"})
    else:
       return render(request,"Admin\District.html",{'dis':dist})


def Deldis(request,did):
    dis=District.objects.get(id=did)    
    dis.delete()
    return redirect('webadmin:dis') 



def DelFeed(request,did):
    feed=Feedback.objects.get(id=did)    
    feed.delete()
    return redirect('webadmin:feed_back') 


def place(request):
    dis=District.objects.all()
    pl=Place.objects.all()
    if request.method=="POST":
        di=District.objects.get(id=request.POST.get("District"))
        Place.objects.create(district=di,place_name=request.POST.get('txt_Place'))
        return render(request,"Admin\Place.html",{'dis':dis,'pl':pl,'msg':"Data Inserted"})
    else:
       return render(request,"Admin\Place.html",{'dis':dis,'pl':pl})  
def Delpal(request,did):
    pl=Place.objects.get(id=did)    
    pl.delete()
    return redirect('webadmin:place')   
def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Admin/AjaxPlace.html",{'pl':pl})    


def Cat(request):
    cat=Category.objects.all()
    if request.method=="POST":
        
        Category.objects.create(category_name=request.POST.get('txt1'))
        return render(request,"Admin\Category.html",{'res':cat,'msg':"Data Inserted"})
    else:
        return render(request,"Admin\Category.html",{'res':cat})  

def DelCat(request,did):
    cat=Category.objects.get(id=did)    
    cat.delete()
    return redirect('webadmin:Category')   

def EditCat(request,eid):
    cat=Category.objects.get(id=eid)
    if request.method=="POST":
        cat.category_name=request.POST.get('txt1')
        cat.save()
        return redirect('webadmin:Category') 
    else:    
         return render(request,"Admin\EditCategory.html",{'res':cat})       

def SubCat(request):
    cat=Category.objects.all()
    subcat=SubCategory.objects.all()
    if request.method=="POST":
        ca=Category.objects.get(id=request.POST.get("Category"))
        SubCategory.objects.create(category=ca,subcat_name=request.POST.get('txt_subcat'))
        return render(request,"Admin\Subcategory.html",{'cat':cat,'subcat':subcat,'msg':"Data Inserted"})
    else:
       return render(request,"Admin\Subcategory.html",{'cat':cat,'subcat':subcat}) 

def Delsub(request,did):
    subcat=SubCategory.objects.get(id=did)    
    subcat.delete()
    return redirect('webadmin:subcategory')   
           
def Ajaxsub(request):
    cat=Category.objects.get(id=request.GET.get('catd'))
    print(cat)
    subcat=SubCategory.objects.filter(category=cat)
    return render(request,"Admin/AjaxSub.html",{'subcat':subcat})  
    
def prod(request):
    cat=Category.objects.all()
    subcat=SubCategory.objects.all()  
    prod=Product.objects.all()
    if request.method=="POST":  
        ca=Category.objects.get(id=request.POST.get('Category'))
        sub=SubCategory.objects.get(id=request.POST.get('subcategory'))
        Product.objects.create(product_name=request.POST.get('txtname'),product_category=ca,product_subcategory=sub,product_photo=request.FILES.get('photo'),product_des=request.POST.get('txtad'),product_price=request.POST.get('price'),stock_qty=request.POST.get('txtstock'))
        return render(request,"Admin\Product.html",{'prod':prod,'cat':cat,'msg':"Data Inserted"})
    else:
      return render(request,"Admin\Product.html",{'prod':prod,'cat':cat}) 

def Delprod(request,did):
    pro=Product.objects.get(id=did)    
    pro.delete()
    return redirect('webadmin:prod')        


def userlist(request):
    newuser=User.objects.all()
    return render(request,"Admin/UserList.html",{'data':newuser})     

def acceptlist(request):
    accorg=Organization.objects.filter(org_vstatus=1)
    return render(request,"Admin/AcceptedList.html",{'data':accorg})    

def rejectlist(request):
    rejorg=Organization.objects.filter(org_vstatus=2)
    return render(request,"Admin/RejectedList.html",{'data':rejorg})   

def DelUser(request,did):
    user=User.objects.get(id=did)       
    user.delete()
    return redirect('webadmin:user')  

def orglist(request):
    neworg=Organization.objects.filter(org_vstatus=0)
    return render(request,"Admin/OrganisationList.html",{'data':neworg})  

def acceptedorg(request):

    if request.method=="POST":
        email=Organization.objects.get(id=request.POST.get('org_email'))
        send_mail( 
            'Respected Sir/Madam', #subject 
            "Your Otp is", #body 
             settings.EMAIL_HOST_USER, 
             [request.POST.get('email')], 
        ) 


    neworg=Organization.objects.filter(org_vstatus=1)
    return render(request,"Admin/AcceptedList.html",{'data':neworg})      

def rejectedorg(request):
    neworg=Organization.objects.filter(org_vstatus=2)
    return render(request,"Admin/RejectedList.html",{'data':neworg})       

# def Delorg(request,did):
#     org=Organization.objects.get(id=did)    
#     org.delete()
#     return redirect('webadmin:organization')                 

def AjaxProduct(request):
    cat=Category.objects.get(id=request.GET.get('catd'))
    subcat=SubCategory.objects.filter(category=cat)
    return render(request,"Admin/AjaxProduct.html",{'subcat':subcat})  
 
# Create your views here.
def Acceptorg(request,did):
    org=Organization.objects.get(id=did)
    org.org_vstatus=1
    org.save()
    name=org.org_name
    email=org.org_email
    send_mail( 
            'Respected Sir/Madam' +name, #subject 
            "Your's request is accepted.You can login with your given Email_ID and Password.", #body 
             settings.EMAIL_HOST_USER, 
             [email], 
        ) 

    return redirect("webadmin:organization")

def RejectOrg(request,did):
    org=Organization.objects.get(id=did)
    org.org_vstatus=2
    org.save()
    name=org.org_name
    email=org.org_email
    send_mail( 
            'Respected Sir/Madam' +name, #subject 
             "Sorry your's request can't be accepted.", #body 
             settings.EMAIL_HOST_USER, 
             [email], 
        ) 
    return redirect("webadmin:organization")

def Delorg(request,did):
    org=Organization.objects.get(id=did)       
    org.delete()
    return redirect('webadmin:acceptorganisation')   

def Delorga(request,did):
    orga=Organization.objects.get(id=did)       
    orga.delete()
    return redirect('webadmin:rejectorganisation')       

  

def Addstock(request,sid):
    prod=Product.objects.get(id=sid)
    stock=int(prod.stock_qty)
    if request.method=="POST":  
       stock=stock+int(request.POST.get('stockqty'))
       prod.stock_qty=stock
       prod.save()
       return redirect('webadmin:prod')  
    else:
        return render(request,"Admin\Stock.html",{'prod':prod})
       


# def Viewmore(request):
#     cat=Category.objects.all()
#     subcat=SubCategory.objects.all()  
#     prod=Product.objects.all()
#     if request.method=="POST":  
#         ca=Category.objects.get(id=request.POST.get('Category'))
#         sub=SubCategory.objects.get(id=request.POST.get('subcategory'))
#         return render(request,"User\ViewMore.html",{'prod':prod,'cat':cat})   

def usercomplaint(request):
    com=Complaint.objects.all()
    return render(request,"Admin/UserComplaint.html",{'data':com})   

def Complaintreply(request,cid):
    reply = Complaint.objects.get(id=cid)
    if request.method=="POST":
        reply.complaint_reply=request.POST.get('txtreply')
        reply.complaint_status=1
        reply.save()
        return redirect('webadmin:complaint')  
    else:
       return render(request,"Admin\ComplaintReply.html")

def userfeedback(request):
    feed=Feedback.objects.all()
    return render(request,"Admin/Feedbacklist.html",{'data':feed})     


def UserReport(request):
    if request.method=="POST":
        frdate=request.POST.get('frdate')
        todate=request.POST.get('todate')
        data=Cart.objects.filter(booking__booking_date__gte=frdate,booking__booking_date__lte=todate)
        return render(request,"Admin/ProdBookingReport.html",{'data':data,'f':frdate,'t':todate}) 
    return render(request,"Admin/ProdBookingReport.html")      


   

def ShowReport(request):
    if request.method=="POST":
        frdate=request.POST.get('frdate')
        todate=request.POST.get('todate')
        data=BookShow.objects.filter(booking_date__gte=frdate,booking_date__lte=todate)
        return render(request,"Admin/ShowBookingReport.html",{'data':data,'f':frdate,'t':todate}) 
    return render(request,"Admin/ShowBookingReport.html")       
          



