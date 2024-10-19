from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard2/", views.dashboard, name="dashboard2"),
    path("predict/", views.predict, name="predict"),
    path("profile/", views.profile, name="profile"),
    path("", views.landingpage, name="landingpage"),
    path("contact/", views.contact_view, name="contact_page"),
    path('crop/<int:image_id>/', views.crop_image, name='crop_image'),
    path('crop/save/<int:image_id>/', views.save_cropped_image, name='save_cropped_image'),
]
