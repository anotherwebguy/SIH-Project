from django.urls import path

from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.register,name='register'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('signin/',views.signin,name='signin')
]