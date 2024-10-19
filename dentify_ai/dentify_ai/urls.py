from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('root/admin/', admin.site.urls),
    path('user/', include('accounts.urls'), name='accounts'),
    path('', include('home.urls'), name='home'),
    path('cropper/', include('cropper.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
