from rest_framework import generics

from apps.habits.models import Habit
from apps.habits.pagination import HabitsPagination
from apps.habits.serializers import HabitSerializer

class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

