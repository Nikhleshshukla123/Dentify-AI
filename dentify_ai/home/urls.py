from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('', views.landingpage, name='landingpage'),
]
