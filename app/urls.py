from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('prof-dashboard/', views.prof_dashboard, name='prof-dash'),
    path('student-dashboard/', views.student_dashboard, name='student-dash'),
    path('prof-quizzes/', views.prof_quizzes, name='prof-quizzes'),
    path('prof-map/', views.prof_map, name='prof-map'),
    path('student-stats/', views.student_stats, name='student-stats')
]

