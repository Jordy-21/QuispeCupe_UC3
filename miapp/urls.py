from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('uc3',views.uc3, name='uc3'),
    path('noticia',views.noticia, name='noticia')   
    ]