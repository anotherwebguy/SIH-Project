from django.urls import path
from . import views

urlpatterns = [
    path('', views.cropPredict, name='cropPredict'),
    path('crops/<str:name>/' , views.crop_profile , name = 'crop_profile'),
]