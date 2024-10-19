# cropper/views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crop_image', pk=form.instance.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'cropper/upload_image.html', {'form': form})

def crop_image(request, pk):
    image = UploadedImage.objects.get(pk=pk)
    return render(request, 'cropper/crop_image.html', {'image': image})

