from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard2/", views.dashboard, name="dashboard2"),
    path("predict/", views.predict, name="predict"),
    path("", views.landingpage, name="landingpage"),
]