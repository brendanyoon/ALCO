from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('pdash/', views.profDashboard, name='prof-dash')

]

