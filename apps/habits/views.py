from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.habits.models import Habit
from apps.habits.pagination import HabitsPagination
from apps.habits.permissions import IsOwnerPermission
from apps.habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """View to create a habit.
       To create you need to enter (at least) place, time and action.
       In case of the tests don't forget to change permissions."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """View to get a list of habits (returns only your own habits).
       Has pagination.
       In case of the tests don't forget to change permissions."""
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """View to get a list of habits (returns only public habits).
       Has pagination.
       In case of the tests don't forget to change permissions."""
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitDetailAPIView(generics.RetrieveAPIView):
    """View to get a particular habit by its id (returns only your own habits).
       In case of the tests don't forget to change permissions."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """View to update a habit by its id (you can update only your own habits).
       In case of the tests don't forget to change permissions."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    """View to delete a habit by its id (you can delete only your own habit).
       In case of the tests don't forget to change permissions."""
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    # In case of test
    # permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
