from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('atracoes/', views.atracoes, name='atracoes'),
    path('historia/', views.historia, name='historia'),
    path('galeria/', views.galeria, name='galeria'),
]