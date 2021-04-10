from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/add-job/', views.addjob, name='addjob'),
    path('questions/', views.questions, name='questions'),
    path('questions/add-new-questions/', views.addquestions, name='addquestions'),
    path('candidate/', views.candidate, name='candidate'),
    path('interview/', views.interview, name='interview'),
]
