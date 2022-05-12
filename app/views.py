#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app.exp import exp
from .models import Student, Completed_Quest

global username

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
    global username
    username = 'xyz@umbc.edu'
    student = Student.objects.get(student_email = username)
    name = student.first_name + ' ' + student.last_name
    return render(request, 'app/student-dashboard.html', context = {'name': name, 'level': exp.GetLevel(student.exp_pts)})

def student_map(request):
    student = Student.objects.get(student_email=username)
    name = student.first_name + ' ' + student.last_name
    xp = student.exp_pts
    return render(request, 'app/student-map.html', context = {'level': exp.GetLevel(xp), 'name': name})

def student_quest(request):
    student = Student.objects.get(student_email=username)
    name = student.first_name + " " + student.last_name
    xp = student.exp_pts
    context = { 'level': exp.GetLevel(xp),
                'name': name }
    return render(request, 'app/student-quest.html', context = context)

def prof_quest(request):
    return render(request, 'app/prof-quest.html')

def student_stats(request):
    student = Student.objects.get(student_email='xyz@umbc.edu')
    xp = student.exp_pts
    level = exp.GetLevel(xp)
    percent = round(exp.ToNextLevelPercent(xp) * 100, 2)
    name = student.first_name + " " + student.last_name

    context = {
        'name': name,
        'xp': xp,
        'level': level,
        'percent': str(percent)+"%",
        'ariapercent': str(percent)
    }

    return render(request, 'app/student-stats.html', context=context)
