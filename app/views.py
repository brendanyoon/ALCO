<<<<<<< HEAD
=======
#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response

>>>>>>> 29d1dc4a964e09f7d8ffb3c0580bd3aebb88de35
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    return render(request, 'app/home.html')
=======
    return render(request, 'app/home.html')

def prof_dashboard(request):
    return render(request, 'app/prof-dashboard.html')


>>>>>>> 29d1dc4a964e09f7d8ffb3c0580bd3aebb88de35
