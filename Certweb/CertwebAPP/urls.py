from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('sobre-mi/', views.about_me, name='about_me'),
]
