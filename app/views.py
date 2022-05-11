#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app.exp import exp

def home(request):
    return render(request, 'app/home.html')

def prof_dashboard(request):
    return render(request, 'app/prof-dashboard.html')

def prof_quizzes(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url']= fs.url(name)

    return render(request, 'app/prof-quizzes.html', context)

def prof_map(request):
    return render(request, 'app/prof-map.html')

def student_dashboard(request):
    return render(request, 'app/student-dashboard.html')

def student_map(request):
    return render(request, 'app/student-map.html')

def student_quiz(request):
    return render(request, 'app/student-quiz.html')

def student_stats(request):
    xp = 125999 #Here, we would get exp from the database. Placeholder number for now
    level = exp.GetLevel(xp)
    percent = round(exp.ToNextLevelPercent(xp) * 100, 2)

    context = {
        'xp': xp,
        'level': level,
        'percent': str(percent)+"%",
        'ariapercent': str(percent)
    }

    return render(request, 'app/student-stats.html', context=context)
