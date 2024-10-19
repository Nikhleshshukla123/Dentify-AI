from django.contrib import admin
from home.models import Prediction
from home.models import ContactMessage


admin.site.register(Prediction)
admin.site.register(ContactMessage)

