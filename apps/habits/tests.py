from rest_framework import status
from rest_framework.test import APITestCase

from apps.habits.models import Habit
from apps.users.models import User


class HabitTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/habits/views"""

    def setUp(self) -> None:
        self.url = '/habits/'
        self.user = User.objects.create(username='test', password='test', telegram='test')
        self.data = {
            'user': self.user,
            'place': 'test',
            'time': '2023-08-11 00:00:00',
            'action': 'test'
        }

        self.habit = Habit.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_habit(self):
        """Habit creation testing """
        data = {
            'user': self.user.pk,
            'place': 'test',
            'time': '2023-08-11 00:00:00',
            'action': 'test'
        }
        response = self.client.post(f'{self.url}create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_2_list_habit(self):
        """Habit list testing """
        response = self.client.get(f'{self.url}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'],
            [{'id': self.habit.pk, 'place': 'test', 'time': '2023-08-11T00:00:00+03:00', 'action': 'test',
              'is_pleasant': False, 'frequency': 1, 'reward': None, 'execution_time': None, 'is_public': False,
              'user': self.user.pk, 'related_habit': None}]
        )

    def test_3_list_habit_public(self):
        """Habit public list testing """
        response = self.client.get(f'{self.url}public/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'],
            []
        )

    def test_4_retrieve_habit(self):
        """Habit retrieve testing """

        response = self.client.get(f'{self.url}{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.habit.pk, 'place': 'test', 'time': '2023-08-11T00:00:00+03:00', 'action': 'test',
             'is_pleasant': False, 'frequency': 1, 'reward': None, 'execution_time': None, 'is_public': False,
             'user': self.user.pk, 'related_habit': None}
        )

    def test_5_update_habit(self):
        """Habit update testing """
        data = {
            'user': self.user.pk,
            'place': 'test1',
            'time': '2023-08-11 00:00:00',
            'action': 'test'
        }

        response = self.client.put(f'{self.url}update/{self.habit.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.habit.pk, 'place': 'test1', 'time': '2023-08-11T00:00:00+03:00', 'action': 'test',
             'is_pleasant': False, 'frequency': 1, 'reward': None, 'execution_time': None, 'is_public': False,
             'user': self.user.pk, 'related_habit': None}
        )

    def test_6_update_partial_habit(self):
        """Habit partial update testing """
        data = {
            'place': 'test2'
        }
        response = self.client.patch(f'{self.url}update/{self.habit.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.habit.pk, 'place': 'test2', 'time': '2023-08-11T00:00:00+03:00', 'action': 'test',
             'is_pleasant': False, 'frequency': 1, 'reward': None, 'execution_time': None, 'is_public': False,
             'user': self.user.pk, 'related_habit': None}
        )

    def test_7_destroy_lesson(self):
        """Habit destroying testing """
        response = self.client.delete(f'{self.url}delete/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Habit.objects.all().exists())
