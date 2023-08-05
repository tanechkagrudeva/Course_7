from django.urls import path

from apps.habits.views import *

app_name = 'habits'

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits'),
]
