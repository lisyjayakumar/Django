from django .urls import path
from home import views
urlpatterns = [
     path('',views.homes),
     path('user/',views.login),
     path('adminlogin/',views.adminlogin),
     path('adminsign/',views.adminsign),
     path('Quizhtml/',views.home),
 
 ]











