from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_temperature/', views.get_temperature, name='get_temperature'),
     path('get_text/', views.get_text, name='get_text'),
    path('save_text/', views.save_text, name='save_text'),


]
