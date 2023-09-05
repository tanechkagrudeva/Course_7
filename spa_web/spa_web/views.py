from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .paginators import HabitsPagination
from .permissions import IsOwnerPermission
from .serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки.
       Для создания необходимо внести минимально: место, время и действие"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Просмотреть список привычек (только собственные привычки).
       Содержит pagination."""

    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотреть список привычек (только собственные привычки).
       Содержит pagination."""

    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitDetailAPIView(generics.RetrieveAPIView):

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки по id (удалить можно только свою привычку).
       При тестировании изменить permissions."""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаление привычки по id (удалить можно только свою привычку).
       При тестировании изменить permissions."""

    permission_classes = [IsAuthenticated, IsOwnerPermission]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)