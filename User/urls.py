from django.urls import path
from User import views
app_name="webuser"

urlpatterns = [
    path('home/',views.Home,name="Home"),
    path('uprofile/',views.UserProfile,name="uprofile"),
    path('edtpro/',views.EditProfile,name="edtpro"),
    path('changepass/',views.ChangePass,name="changepass"),
    path('searchproduct/',views.SearchProduct,name="searchproduct"),
   
    path('mycart/', views.Mycart,name="mycart"),

    path('ajaxproduct/', views.AjaxProduct,name="Ajax-product"),
    path('cart/<int:pid>',views.Addtocart,name="cart"),
    path('delpdt/<int:pdid>',views.del_pdt,name="del_pdt"),

    path('complaint/', views.complaint,name="complaint"), 
    path('reply/', views.Complaintreply,name="reply"),
    path('show/', views.Activeshow,name="show"),
    path('bookshow/<int:shid>',views.book_show,name="book_show"),
    path('payshow/<int:pid>',views.pay_show,name="pay_show"),

    path('feed/', views.FeedBack,name="feed_back"), 
    path('quantity/', views.QuantityUpdate,name="quantity-update"), 
    path('baddress/', views.BookingAddress,name="book_address"),
    path('spaid/', views.PaidShow,name="paid_show"), 
    path('delpshow/<int:did>', views.Delpshow,name="del_pshow"),
    path('premove/', views.premove,name="premove"),
    path('prodpay/',views.prod_pay,name="ProductPay"),
    path('pbill/',views.combinedbill,name="prodbill"),
    path('myprod/',views.BookedList,name="myprod"),
    path('delbplist/<int:did>',views.DelBookedList,name="delbplist"),
    path('certificate/<int:pid>',views.certi,name="certificate"),
    path('res/<int:pid>', views.showresult,name="sresult"),
    path('loader/', views.Load,name="loader"),
    path('success/', views.success1,name="success"),
    path('loader/', views.Loader,name="loader2"),
    path('successor/', views.success2,name="successor"),


    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),


    path('logout/',views.logout,name="logout")
]