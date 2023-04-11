from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('initial/', views.initial, name= "initial"),
    path('explora/', views.exploracion, name= "explora"),
    path('form/', views.formulario, name= "form"),
    path('juega/', views.juego, name= "juega"),
    path('validar/', views.valida, name= "validar"),
    
]