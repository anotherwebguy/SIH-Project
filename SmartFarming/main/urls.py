from django.urls import path

from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('signin/',views.signin,name='signin')
]