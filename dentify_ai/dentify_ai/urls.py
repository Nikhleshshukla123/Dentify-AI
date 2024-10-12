from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('root/admin/', admin.site.urls),
    path('', include('accounts.urls'), name='accounts'),
    path('dashboard/', include('home.urls'), name='home'),
]
