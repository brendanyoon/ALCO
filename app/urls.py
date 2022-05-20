from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('prof-dashboard/', views.prof_dashboard, name='prof-dash'),
    path('student-dashboard/', views.student_dashboard, name='student-dash'),
    path('prof-quizzes/', views.prof_quizzes, name='prof-quizzes'),
    path('prof-map/', views.prof_map, name='prof-map'),
    path('prof-quest/', views.prof_quest, name='prof-quest'),
    path('student-stats/', views.student_stats, name='student-stats'),
    path('student-map/', views.student_map, name='student-map'),
    path('student-quest/', views.student_quest, name='student-quest'),
    path('prof-quest-dashboard/', views.prof_quest_dashboard, name='prof-quest-dashboard'),
    path('prof-quest/quest/<str:quest_title>/', views.quest, name='quest'),
    path('prof-quest/create-obstacle/<str:quest_title>/', views.create_obstacle, name='prof-obstacle-create')
]

