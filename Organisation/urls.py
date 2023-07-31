from django.urls import path
from Organisation import views
app_name="weborganisation"

urlpatterns = [
    path('home/',views.Home,name="Home"),
    path('uprofile/',views.OrgProfile,name="uprofile"),
    path('edtpro/',views.EditProfile,name="edtpro"),
    path('changepass/',views.ChangePass,name="changepass"),
    path('shw/',views.Show,name="shw"),
    path('show/<int:did>', views.DelShow,name="delshow"),
    path('judge/',views.Judge,name="judge"),
    path('jo/<int:did>', views.DelJudge,name="deljudge"),
    path('res/<int:pid>', views.result,name="result"),
    path('spaid/<int:shid>', views.BookedList,name="paid_show"), 
    path('shwlist/',views.ShowList,name="shwlist"),
    path('Login/',views.Logout,name="Login"),
    path('logout/',views.logout,name="logout"),

    path('Chat/<int:cid>/', views.chat, name="Chat-doctor"),
    path('loadchat/', views.loadchat, name="load-chat"),
]
   

   