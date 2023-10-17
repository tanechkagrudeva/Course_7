from rest_framework.generics import ListAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.habits.models import Habit
from apps.habits.serializers import HabitSerializer
from apps.habits.services import get_schedule
from apps.users.permissions import IsOwner
from apps.habits.tasks import send_tg_notification
from dotenv import load_dotenv

load_dotenv()


# Create your views here.
class HabitPublicListAPIView(ListAPIView):
    """
    API View for display the list of all public habits.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Returns queryset depending on the publicity of the habit."""
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitIndListAPIView(ListAPIView):
    """
    API View for display the list of user`s habits only.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Habit.objects.filter(owner=self.request.user)
        return queryset


class HabitCreateAPIView(CreateAPIView):
    """
    API View for create the habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()

        get_schedule(action=new_habit.action, frequency=new_habit.frequency)
        send_tg_notification.delay()


class HabitUpdateAPIView(UpdateAPIView):
    """
    API View for update the habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """
    API View for delete the habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]