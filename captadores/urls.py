from django.urls import path
from . import views

app_name = 'captadores'

urlpatterns =[ 

    path('', views.home, name = 'home'),
    path('home2', views.home2, name = 'home2'),
    path('form_captador', views.form_captador, name = 'form_captador'),
    path('criar_captador', views.criar_captador, name = 'criar_captador'),
    path('lista_captadores', views.lista_captadores, name = 'lista_captadores')

    
]