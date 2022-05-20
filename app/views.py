#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response
from .forms import *
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app.exp import exp
from .models import *
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

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
    return render(request, 'app/student-quest.html')

def prof_quest(request):
    all_quests = Quest.objects.all()
    quest_create_form = Quest_Creation_Form()
    if request.method == "POST":
        quest_create_form = Quest_Creation_Form(request.POST)

        if quest_create_form.is_valid():
            quest_create_form.save()
            quest_title = request.POST.get('title')
            
            return HttpResponseRedirect('/prof-quest')
        
    else:
        quest_create_form = Quest_Creation_Form()  

    context = {'all_quests': all_quests, 'quest_create_form': quest_create_form}
    return render(request, 'app/prof-quest.html', context)

def quest(request, quest_title):
    quest = Quest.objects.get(title=quest_title)
    all_obstacles = Obstacle.objects.filter(quest_id=quest)
    num_obstacle_created = all_obstacles.count()

    context = {'quest':quest, 'all_obstacles':all_obstacles, 'num_obstacle_created':num_obstacle_created}
    return render(request, 'app/prof-quest-create-dashboard.html', context)

def prof_quest_dashboard(request):
   # MC_form_set = inlineformset_factory(Obstacle, Multiple_Choice)
   # MA_form_set = inlineformset_factory(Obstacle, Multiple_Answers)
    quest = "hi"

def create_obstacle(request, quest_title):
    quest = Quest.objects.get(title=quest_title)
    obstacle_create_form = Obstacle_Creation_Form()
    mc_create_form = Multiple_Choice_Creation_Form()

    if request.method == "POST":

        obstacle_create_form = Obstacle_Creation_Form(request.POST)
        #mc_create_form = Multiple_Choice_Creation_Form(request.POST)

        if obstacle_create_form.is_valid():
            obstacle_create_form.save()
            #mc_create_form.save()

            #return reverse('prof-quest/create-obstacle', args=[quest_title])
        
    else:
        obstacle_create_form = Obstacle_Creation_Form()  
        #mc_create_form = Multiple_Choice_Creation_Form()

    context = {'quest': quest, 'obstacle_create_form': obstacle_create_form}
    return render(request, 'app/prof-obstacle-create.html', context)


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

