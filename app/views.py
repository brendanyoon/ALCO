#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response
from .forms import Quest_Creation_Form, Question_Form_Student
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

def student_quest(request):
    question_form_student = Question_Form_Student()
    return render(request, 'app/student-quest.html', {'question_form_student': question_form_student})

def prof_quest(request):
    quest_create_form = Quest_Creation_Form()
    if request.method == "POST":
        quest_create_form = Quest_Creation_Form(request.POST)

        if quest_create_form.is_valid():
            quest = quest_create_form.save()
            quest.save()

    else:
        quest_create_form = Quest_Creation_Form()

    return render(request, 'app/prof-quest.html', {'quest_create_form': quest_create_form})

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

