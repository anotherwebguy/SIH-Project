from django.urls import path

from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('home/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('signin/',views.signin,name='signin')
]