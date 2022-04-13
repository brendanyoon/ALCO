from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')

def prof_dashboard(request):
    return render(request, 'app/pDash.html')