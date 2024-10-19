# cropper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('crop/<int:pk>/', views.crop_image, name='crop_image'),
]
