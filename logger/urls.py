# logger/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('daily/', views.dailyUpdate, name='daily'),
    path('weekly/', views.weeklyUpdate, name='weekly'),
    path('success/', views.successView, name='success'),
]