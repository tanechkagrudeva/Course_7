from django.urls import path

from apps.habits.apps import HabitConfig
from apps.habits.views import HabitPublicListAPIView, HabitUpdateAPIView, HabitDestroyAPIView, HabitCreateAPIView, \
    HabitIndListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('public/', HabitPublicListAPIView.as_view(), name='public_habits_list'),
    path('my/', HabitIndListAPIView.as_view(), name='ind_habits_list'),
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete_habit'),
]