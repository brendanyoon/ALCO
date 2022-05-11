from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('prof-dashboard/', views.prof_dashboard, name='prof-dash'),
    path('prof-quizzes/', views.prof_quizzes, name='prof-quizzes'),
    path('prof-map/', views.prof_map, name='prof-map'),
    path('student-dashboard/', views.student_dashboard, name='student-dash'),
    path('student-map/', views.student_map, name='student-map'),
    path('student-quiz', views.student_quiz, name='student-quiz'),
    path('student-stats/', views.student_stats, name='student-stats')
]
