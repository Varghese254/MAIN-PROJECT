from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import User,Organization
from Organisation.models import *
from User.models import *
from django.core.mail import send_mail 
from django.conf import settings 
import random
#Ajaxsil session validation Vendaaa

# session illel page Work Akathe erikan an ath use cheyunnee
#uid marum oro appilum
# Create your views here.
def Home(request):
    if 'uid' in request.session:
        user=User.objects.get(id=request.session["uid"])
        return render(request,"User/HomePage.html",{'data':user})
    else:
        return redirect("webguest:login")
    
def UserProfile(request):
    if 'uid' in request.session:
        pro=User.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'data':pro})
    else:
        return redirect("webguest:login")    
  

def EditProfile(request):
    pro=User.objects.get(id=request.session["uid"])
    if request.method=="POST":
        pro.user_name=request.POST.get('txt_name')
        pro.user_contact=request.POST.get('txt_contact')
        pro.user_address=request.POST.get('txt_address')
        pro.save()
        return redirect("webuser:uprofile")
    else:
        return render(request,"User/EditProfile.html",{'data':pro})  


def ChangePass(request):
    if request.method=="POST":
        usercount=User.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcur')).count()
        if usercount>0:
            user=User.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcur'))
            user.user_password=request.POST.get('txtnew')
            user.save()
            return redirect("webuser:Home")
    else:
        return render(request,"User/ChangePassword.html")    

def SearchProduct(request):
    ca=Category.objects.all()
    sub=SubCategory.objects.all()
    prod=Product.objects.all()
    return render(request,"User/SearchProduct.html",{'ca':ca,'sub':sub,'prod':prod})




def AjaxProduct(request):
    if request.GET.get('sid')!="":
        sub=SubCategory.objects.get(id=request.GET.get('sid'))
        prod=Product.objects.filter(product_subcategory=sub)
        return render(request,"User/AjaxProduct.html",{'pr':prod})
    else:
        cat=Category.objects.get(id=request.GET.get('cid'))
        prod=Product.objects.filter(product_subcategory__category=cat)
        return render(request,"User/AjaxProduct.html",{'pr':prod})


def Addtocart(request,pid):
    proddata=Product.objects.all()
    ca=Category.objects.all()
    sub=SubCategory.objects.all()
    message=""
    userid=User.objects.get(id=request.session["uid"])
    prod=Product.objects.get(id=pid)
    

    bcount=Booking.objects.filter(user=userid,booking_status=0).count()
    if bcount>0:
        bobject=Booking.objects.get(user=userid,booking_status=0)
        ccount=Cart.objects.filter(booking=bobject,product=prod).count()
        if ccount>0:
            message="AlreadyAddedtoCart"
            return render(request,"User/SearchProduct.html",{'ca':ca,'sub':sub,'prod':proddata,'message':message})
        else:
            Cart.objects.create(booking=bobject,product=prod)
            message="AddedtoCart"
            return render(request,"User/SearchProduct.html",{'ca':ca,'sub':sub,'prod':proddata,'message':message})
    else:
        Booking.objects.create(user=userid)
        bobject=Booking.objects.get(user=userid,booking_status=0,cart_status=0)
        Cart.objects.create(booking=bobject,product=prod)
        message="AddedtoCart"
        return render(request,"User/SearchProduct.html",{'ca':ca,'sub':sub,'prod':proddata,'message':message})



  



def Mycart(request,pid):
    userid=User.objects.get(id=request.session["uid"])
    cart=Cart.objects.filter(booking__user=userid)


    #bookings=Booking.objects.get(user=userid,cart_status=0)
    if request.method=="POST":
        return redirect("webuser:book_address")
    else:
        return render(request,"User/Mycart.html",{'data':cart})  


def del_pdt(request,pdid):
    Cart.objects.get(id=pdid).delete()
    return redirect('webuser:mycart')
  
           
            


def BookingAddress(request):
    pro=User.objects.get(id=request.session["uid"])
    bookingid=Booking.objects.filter(user=pro).last()
    qty=Cart.objects.all()
    prod=Product.objects.all()
    # print(total)
    #qty=Cart.objects.get(id=request.POST.get('cart_qty'))
   # price=Product.objects.get(id=request.POST.get('product_price'))

    if request.method=="POST":
        # pro.user_name=request.POST.get('txt_address')
        # pro.user_contact=request.POST.get('txt_contact')
        # pro.user_address=request.POST.get('txt_pin')
        # pro.save()
        
        ProdBooking.objects.create(user=pro,booking=bookingid,booking_address=request.POST.get('txt_address'),
                booking_contact=request.POST.get('txt_contact'),booking_pincode=request.POST.get('txt_pin'))
      # return redirect('webuser:ProductPay',{'data':prod})  
        return redirect("webuser:ProductPay")
    else:
        return render(request,"User/BookingAddress.html",{'data':pro}) 


           
     
 

def complaint(request):
    com=Complaint.objects.all()
    neworg=Organization.objects.filter(org_vstatus=1)
    user=User.objects.get(id=request.session['uid'])
    if request.method=="POST":
        orgid=request.POST.get('organisation')
        org=Organization.objects.get(id=orgid)
        Complaint.objects.create(organisation_name=org,complaint_title=request.POST.get('complaint'),
            complaint_details=request.POST.get('txtdetails'),user_id=user)
        return render(request,"User\Complaint.html",{'res':com,'Org':neworg}) 
    else:
         return render(request,"User\Complaint.html",{'res':com,'Org':neworg})


def Complaintreply(request):
    userid=User.objects.get(id=request.session["uid"])
    com=Complaint.objects.filter(user_id=userid)
    return render(request,"User/ComplaintReply.html",{'data':com})    

def Activeshow(request):
    usr=User.objects.get(id=request.session['uid'])
    show=ScheduleShow.objects.all()
    acshow=ScheduleShow.objects.all()
    return render(request,"User/NewShows.html",{'Show':acshow})           

         
def book_show(request,shid):
    usr=User.objects.get(id=request.session['uid'])
    show=ScheduleShow.objects.all()
    var=ScheduleShow.objects.get(id=shid)
    book=ScheduleShow.objects.filter(id=shid)
    bcount=BookShow.objects.filter(schedule=var,user=usr).count()
    return render(request,"User/BookMyShow.html",{'data':show,'Book':book,'bcount':bcount})
    
     
def pay_show(request,pid):
    var=BookShow.objects.all()
    show=ScheduleShow.objects.get(id=pid)
    usr=User.objects.get(id=request.session['uid'])


    if request.method=="POST":
        show.schedule_status=1
        show.save()
        BookShow.objects.create(schedule=show,booking_sts=1,payment_sts=1,user=usr)


       # return redirect('webuser:paid_show')
        return render(request,"User/Load.html")
    else:
        return render(request,"User/ShowPay.html")



def Load(request):
   return redirect('webuser:success')

def success1(request):
    return render(request,"User/Success.html")


def FeedBack(request):
    feed=Complaint.objects.all()
    neworg=Organization.objects.filter(org_vstatus=1)
    user=User.objects.get(id=request.session['uid'])
    if request.method=="POST":
        orgid=request.POST.get('organisation')
        org=Organization.objects.get(id=orgid)
        Feedback.objects.create(organisation_name=org,feedback_content=request.POST.get('feedback'),
           user_id=user)
        return render(request,"User\Feedback.html",
        
        {'res':feed,'Org':neworg}) 
    else:
         return render(request,"User\Feedback.html",{'res':feed,'Org':neworg})    



def QuantityUpdate(request):
    cid=Cart.objects.get(id=request.GET.get('ALT'))
    cid.cart_qty=request.GET.get('QTY')
    cid.save()
    return redirect("webuser:mycart")


def ShowBook(request):
    book=Organization.objects.filter(schedule_status=1)
    return render(request,"User/ShowPay.html",{'data':book}) 


def PaidShow(request):
    userid=User.objects.get(id=request.session["uid"])
    pshow=BookShow.objects.filter(user=userid)
    return render(request,"User/PaidListOfShows.html",{'data':pshow})  


def Delpshow(request,did):
    org=BookShow.objects.get(id=did)       
    org.delete()
    return redirect('webuser:paid_show')         






def premove(request):
    Cart.objects.get(id=request.GET.get('QTY')).delete()
    return redirect("webuser:mycart")


# def BookingAddress(request):
    
#     usr=User.objects.get(id=request.session['uid'])
#     if request.method=="POST":
#         ProdBooking.objects.create(user=usr,booking_address=request.POST.get('txt_address'),
#                 booking_contact=request.POST.get('txt_contact'),booking_pincode=request.POST.get('txt_pin'))
#         return redirect('webuser:ProductPay')      
#     else:
#         return render(request,"User/BookingAddress.html")



def prod_pay(request):
    usr=User.objects.get(id=request.session['uid'])
    bookingid=Booking.objects.filter(user=usr).last()
    if request.method=="POST":
        bookingid.payment_status=1
        bookingid.booking_status=1
        bookingid.cart_status=1
        
        bookingid.save()
       # return redirect('webuser:ProductPay')  
        #return redirect("webuser:prodbill")
        return render(request,"User/Loader.html")
    else:
            
        return render(request,"User/ProductPay.html")



def Loader(request):
       return redirect('webuser:successor')

def success2(request):
    return render(request,"User/Successor.html")        

def combinedbill(request):
    usr=User.objects.get(id=request.session['uid'])
    bookingid=Booking.objects.filter(user=usr).last()
    data=Cart.objects.filter(booking=bookingid)

    cartcount=Cart.objects.filter(booking=bookingid).count()   
    total=0
    for i in data:
        total=total+(int(i.cart_qty)*int(i.product.product_price))
        print(total)

    return render(request,"User/CombinedBill.html",{'data':data,'tot':total,'detail':usr})


def BookedList(request):
    usr=User.objects.get(id=request.session['uid'])
    bookingid=Booking.objects.filter(user=usr).last()
    data=Cart.objects.filter(booking=bookingid)
    return render(request,"User/BookedList.html",{'data':data,'detail':usr})     


def DelBookedList(request,did):
    Prod=Cart.objects.get(id=did)    
    Prod.delete()
    return redirect('webuser:myprod')  


def certi(request,pid):
    usr=User.objects.get(id=request.session['uid'])
    bookingid=BookShow.objects.filter(user=usr).last()
    var=Result.objects.filter(booking=bookingid)
    return render(request,"User/ShowCertificate.html",{'judge':var})   


def showresult(request,pid):

    usr=User.objects.get(id=request.session['uid'])
    bookingid=BookShow.objects.filter(user=usr).last()
    var=Result.objects.filter(booking=bookingid)


    # org=Organization.objects.get(id=request.session['oid'])
    # show=ScheduleShow.objects.all()
    # bshow=BookShow.objects.get(id=pid)
    # var=Result.objects.all()
    # userid=bshow.user.id
    return render(request,"User\ShowResult.html",{'judge':var}) 
    
          
def logout(request):
    del request.session["uid"]
    return redirect("webguest:login")




def chatuser(request, cid):
    chatobj = BookShow.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        
        ciedobj = Organization.objects.get(id=cied)
        sobj = User.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_user=sobj, to_org=ciedobj, content=content, from_org=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = Organization.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = User.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_user u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_org_id=%s or c.to_org_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/LoadChat.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})