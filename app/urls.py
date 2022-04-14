from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='app-home')
]
=======
    path('', views.home, name='app-home'),
    path('prof-dashboard/', views.prof_dashboard, name='prof-dash')
]

>>>>>>> 29d1dc4a964e09f7d8ffb3c0580bd3aebb88de35
