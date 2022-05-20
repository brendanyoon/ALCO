#imports from Django rest_framework
#import requests
#import time
#from rest_framework import status
#from rest_framework import Response

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app.exp import exp
from .models import Student, Completed_Quest
from .forms import Question_Form_Student

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
        context['url'] = fs.url(name)

    return render(request, 'app/prof-quizzes.html', context)


# This function is currently not working -- something to troubleshoot in a future iteration
def prof_quizzes2(request):
    quizzes = Quiz.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof_quizzes')
    else:
        form = QuizForm()
    return render(request, 'app/prof-quizzes2.html', {
        'form': form,
        'quizzes': quizzes
    })

def prof_map(request):
    return render(request, 'app/prof-map.html')

def student_dashboard(request):
    student = Student.objects.get(student_email='xyz@umbc.edu')
    name = student.first_name
    xp = student.exp()
    return render(request, 'app/student-dashboard.html', context={'name': name, 'level': exp.GetLevel(xp)})

def student_map(request):
    xp = 125999
    return render(request, 'app/student-map.html', context={'level': exp.GetLevel(xp)})

def student_quest(request):
    student = Student.objects.get(student_email='xyz@umbc.edu')
    xp = student.exp()
    question_form_student = Question_Form_Student()
    context = {'level': exp.GetLevel(xp), 'question_form_student': question_form_student}

    return render(request, 'app/student-quest.html', context=context)

def prof_quest(request):
    return render(request, 'app/prof-quest.html')

def student_stats(request):
    student = Student.objects.get(student_email='xyz@umbc.edu')
    xp = student.exp_pts
    level = exp.GetLevel(xp)
    percent = round(exp.ToNextLevelPercent(xp) * 100, 2)

    context = {
        'xp': xp,
        'level': level,
        'percent': str(percent)+"%",
        'ariapercent': str(percent)
    }

    return render(request, 'app/student-stats.html', context=context)


def student_fight(request):
    return render(request, 'app/student-fight-demo.html')