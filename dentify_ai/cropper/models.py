from django.db import models

# cropper/models.py
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')

