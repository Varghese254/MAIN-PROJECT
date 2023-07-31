from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Organisation.models import *
from User.models import *


def Home(request):
    if 'oid' in request.session:
     pro=Organization.objects.get(id=request.session["oid"])
    return render(request,"Organisation/HomePage.html",{'data':pro})

def OrgProfile(request):
    if 'oid' in request.session:
     pro=Organization.objects.get(id=request.session["oid"])
    return render(request,"organisation/MyProfile.html",{'data':pro})    

def EditProfile(request):
    pro=Organization.objects.get(id=request.session["oid"])
    if request.method=="POST":
        pro.org_name=request.POST.get('txt_name')
        pro.org_contact=request.POST.get('txt_contact')
        pro.org_address=request.POST.get('txt_address')
        pro.save()
        return redirect("weborganisation:uprofile")
    else:
        return render(request,"organisation/EditProfile.html",{'data':pro})  


def ChangePass(request):
    if request.method=="POST":
        organizationcount=Organization.objects.filter(id=request.session["oid"],user_password=request.POST.get('txtcur')).count()
        if organizationcount>0:
            user=Organization.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcur'))
            user.user_password=request.POST.get('txtnew')
            user.save()
            return redirect("weborganisation:Home")
    else:
        return render(request,"organisation/ChangePassword.html")                
    
def Show(request):
    pro=Organization.objects.get(id=request.session["oid"])
    dis=District.objects.all()
    shw=ScheduleShow.objects.all()  
    if request.method=="POST":  
        p=Place.objects.get(id=request.POST.get('place'))
        org=Organization.objects.get(id=request.session["oid"])
        ScheduleShow.objects.create(schedule_title=request.POST.get('txtname'),schedule_date=request.POST.get('date'),schedule_time=request.POST.get('time'),place=p,schedule_venue=request.POST.get('txtad'),schedule_details=request.POST.get('details'),schedule_poster=request.FILES.get('photo'),organisation=org,schedule_status='0')
        return redirect('weborganisation:shw')
    else:
      return render(request,"Organisation\ScheduleShow.html",{'dis':dis,'SHW':shw})    

def DelShow(request,did):
    show=ScheduleShow.objects.get(id=did)       
    show.delete()
    return redirect('weborganisation:shw') 


def Logout(request):
    return redirect('webguest:Login')       




def Judge(request):
    org=Organization.objects.get(id=request.session['oid'])
    Judge=AddJudge.objects.filter(organisation=org)
    if request.method=="POST":
        AddJudge.objects.create(organisation=org,judge_name=request.POST.get('txt_name'),judge_photo=request.FILES.get('photo'))
        return render(request,"Organisation\AddJudges.html",{'judge':Judge})
    else:
      return render(request,"Organisation\AddJudges.html",{'judge':Judge})    



def DelJudge(request,did):
    jo=AddJudge.objects.get(id=did)       
    jo.delete()
    return redirect('weborganisation:judge')    



def result(request,pid):
    org=Organization.objects.get(id=request.session['oid'])
    show=ScheduleShow.objects.all()
    bshow=BookShow.objects.get(id=pid)
    var=Result.objects.all()
    userid=bshow.user.id
    usr=User.objects.get(id=userid)

    if request.method=="POST":
        bshow.result_sts=1
        bshow.save()
        Result.objects.create(result_position=request.POST.get('txt_num'),user=usr,booking=bshow)
    return render(request,"Organisation\ShowResult.html",{'judge':var})
    # else:
    #   return render(request,"Organisation\ShowResult.html",{'judge':data})  
            


def BookedList(request,shid):
    # pshow=BookShow.objects.all()
    usr=User.objects.all()
   # bookingid=Booking.objects.filter(user=usr).last()
   # book=Organization.objects.filter(schedule_status=1)
    orgrid=ScheduleShow.objects.get(id=shid)
    pshow=BookShow.objects.filter(schedule=orgrid)
 
    return render(request,"Organisation/BookedList.html",{'data':pshow,'dat':usr})                 



def ShowList(request):
    orgrid=Organization.objects.get(id=request.session["oid"])
    lshow=ScheduleShow.objects.filter(organisation=orgrid)
    return render(request,"Organisation/ViewScheduledList.html",{'data':lshow})  




def chat(request, cid):
    chatobj = BookShow.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")

        
        # print(cied)
        ciedobj = User.objects.get(id=cied)
        sobj = Organization.objects.get(id=request.session["oid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        Chat.objects.create(
            from_org=sobj, to_user=ciedobj, content=content, from_user=None, to_org=None)


       

        return render(request, 'Organisation/Chat.html', {"chatobj": chatobj,'count':ccount})
    else:
        return render(request, 'Organisation/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = User.objects.get(id=cid)
    # print(userobj)
    sid = request.session["oid"]
    # print(sid)
    suserobj = Organization.objects.get(id=request.session["oid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_organization u on (u.id=c.from_org_id) or (u.id=c.to_org_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Doctor/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def logout(request):
    del request.session["oid"]
    return redirect("webguest:login")
