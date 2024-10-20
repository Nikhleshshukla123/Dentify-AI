from django.contrib import admin
from home.models import Prediction
from home.models import ContactMessage
from home.models import Image 

admin.site.register(Prediction)
admin.site.register(ContactMessage)
admin.site.register(Image)


