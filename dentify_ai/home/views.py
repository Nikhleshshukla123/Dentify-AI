from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from home.models import Prediction

@login_required
def home(request):
    # check user verified status
    if request.user.verified:
        return HttpResponse("Welcome to the Dentify AI platform!")
    
    return redirect('login')

def landingpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home/landingpage.html')

@login_required(login_url='login')
def dashboard(request):
    history = Prediction.objects.filter(user=request.user)[:10]
    return render(request, 'home/dashboard2.html', context={'history':history})

@login_required(login_url='login')
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        file = request.FILES.get('xray_file')
        print(file)
        if file:
            return JsonResponse({"message": "Prediction successful"})
    return JsonResponse({"message": "Prediction failed"}, status=400)

@login_required(login_url='login')
def profile(request):
    return render(request, 'home/profile.html')
