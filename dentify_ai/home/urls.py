from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard2/", views.dashboard, name="dashboard2"),
    path("predict/", views.predict, name="predict"),
    path("profile/", views.profile, name="profile"),
    path("", views.landingpage, name="landingpage"),
    path("contact/", views.contact_view, name="contact_page"),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
]
