from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
