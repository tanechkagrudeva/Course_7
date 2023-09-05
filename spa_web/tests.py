from django.test import TestCase
from users.models import User
from .models import Habit, Place


class HabitCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com',
                                        password='testpassword')
        self.place = Place.objects.create(place='Test Place',
                                          user=self.user)

    def test_create_habit(self):
        habit_data = {
            'user': self.user,
            'place': self.place,
            'action': 'Test Action',
            'period': 7,
            'reward': 'Test Reward',
            'duration': 100,
        }
        Habit.objects.create(**habit_data)
        self.assertEqual(Habit.objects.count(), 1)

    def test_read_habit(self):
        habit_data = {
            'user': self.user,
            'place': self.place,
            'action': 'Test Action',
            'period': 7,
            'reward': 'Test Reward',
            'duration': 3600,
        }
        habit = Habit.objects.create(**habit_data)
        read_habit = Habit.objects.get(id=habit.id)
        self.assertEqual(read_habit.action, 'Test Action')

    def test_update_habit(self):
        habit_data = {
            'user': self.user,
            'place': self.place,
            'action': 'Test Action',
            'period': 7,
            'reward': 'Test Reward',
            'duration': 3600,
        }
        habit = Habit.objects.create(**habit_data)
        habit.action = 'Updated Action'
        habit.save()
        updated_habit = Habit.objects.get(id=habit.id)
        self.assertEqual(updated_habit.action, 'Updated Action')

    def test_delete_habit(self):
        habit_data = {
            'user': self.user,
            'place': self.place,
            'action': 'Test Action',
            'period': 7,
            'reward': 'Test Reward',
            'duration': 3600,
        }
        habit = Habit.objects.create(**habit_data)
        habit.delete()
        self.assertEqual(Habit.objects.count(), 0)