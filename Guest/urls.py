from django.urls import path
from Guest import views
app_name="webguest"
urlpatterns = [
   path('reg/', views.reg,name="reg"),
   path('oreg/', views.oreg,name="oreg"),
   path('login/', views.Login,name="login"),
   path('forgotpass/', views.ForgotPass,name="forgotpass"), 
   path('validateotp/', views.ValidateOtp,name="validateotp"), 
   path('createpass/', views.CreatePass,name="createpass"),
   
   ]