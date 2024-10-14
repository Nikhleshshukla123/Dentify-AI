from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    # if user logged in
    if request.user.is_authenticated:
        return HttpResponse("Welcome to the Dentify AI platform!")
    
    return redirect('login')

def landingpage(request):
    return render(request, 'home/landingpage.html')
