from django.urls import path
from rest_framework.routers import SimpleRouter
from apps.habits.views import *

app_name = 'habits'

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits'),
]
