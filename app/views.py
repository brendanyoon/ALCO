#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')

def prof_dashboard(request):
    return render(request, 'app/prof-dashboard.html')

def student_dashboard(request):
   return render(request, 'app/student-dashboard.html')
