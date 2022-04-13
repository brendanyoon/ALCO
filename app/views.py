from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')

def profDashboard(request):
    return render(request, 'app/pDash.html')