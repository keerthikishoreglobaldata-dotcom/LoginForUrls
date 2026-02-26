from django.contrib import admin
from django.urls import path
from .views import home,register,login_view,logout_view,change_password,excel_data

urlpatterns = [
    path('', home,name='home'),
    path('login/',login_view ,name='login'),
    path('register/',register ,name='register'),
    path('logout/',logout_view ,name='logout'),
    path('change_password/',change_password ,name='change_password'),
    path('profile_data/',excel_data ,name='profile_data'),
]
