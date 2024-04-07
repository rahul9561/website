from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path('', views.index, name="home"),
   # path('send/', views.send_message, name='send_message'),
   path('login.html', views.login, name="login"),
   path('Forget.html', views.forget, name="forget"),
   path('Profile.html', views.profile, name="profile"),
]