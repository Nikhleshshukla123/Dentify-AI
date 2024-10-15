from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('predict/', views.predict, name='predict'),
    path('profile/', views.profile, name='profile'),
    path('', views.landingpage, name='landingpage'),
]
