from django.urls import path

from .views import HabitListAPIView, HabitPublicListAPIView, HabitDetailAPIView, HabitCreateAPIView, \
    HabitUpdateAPIView, HabitDeleteAPIView

app_name = 'spa_web'

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits'),
    path('public/', HabitPublicListAPIView.as_view(), name='habits_public'),
    path('<int:pk>/', HabitDetailAPIView.as_view(), name='habit'),
    path('create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),
]
