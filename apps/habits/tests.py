from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.habits.models import Habit
from apps.users.models import User


class HabitTestCase(APITestCase):

    def create_user(self):
        self.user = User.objects.create(
            email="test@gmail.com"
        )
        self.user.set_password('123qwe')
        self.user.save()

    def setUp(self) -> None:
        self.create_user()
        self.habit = Habit.objects.create(
            owner=self.user,
            place="здесь",
            time="10:00:00",
            action="делать анжуманя",
            reward="физическое развитие",
            eta=120,
            frequency=1
        )
        self.pleasant_habit = Habit.objects.create(
            owner=self.user,
            place="гроб",
            time="10:00:00",
            action="полежать",
            eta=120,
            is_pleasant=True,
            frequency=1
        )

    def test_habit_public_list(self):
        """ Test for getting list of public habit. """

        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('habit:public_habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 0,
                "next": None,
                "previous": None,
                "results": []
            }
        )

    def test_habit_ind_list(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('habit:ind_habits_list')
        )

        self.assertFalse(
            response.json()['results'][0]['is_public']
        )

        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_create_habit(self):
        data = {
            "place": "на природе",
            "time": "10:00:00",
            "action": "пойти к реке",
            "is_pleasant": True,
            "frequency": 7,
            "eta": 120,
        }

        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('habit:create_habit'),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Habit.objects.all().count(),
            3
        )

        self.assertTrue(
            Habit.objects.get(pk=2).is_pleasant
        )

    def test_update_habit(self):
        data = {
            "reward": "поклониться земле",
            "frequency": 2,
            "eta": 100
        }
        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIsNone(
            response.json()['related_habit']
        )

    def test_delete_habit(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse('habit:delete_habit', kwargs={'pk': self.habit.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    # test validators
    def test_eta_validator(self):
        data = {
            "eta": 200,
            "frequency": 1
        }

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Время выполнения привычки не может превышать 120 секунд или быть меньше 0.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_frequency_validator(self):
        data = {
            "eta": 120,
            "frequency": 8
        }

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Нельзя выполнять привычку реже, чем 1 раз в 7 дней.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_related_habit_validator(self):
        data = {
            "eta": 120,
            "frequency": 1,
            "related_habit": self.habit.pk
        }

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Связанные привычки могут быть только приятными.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_pleasant_habit_validator(self):

        data = {
            "eta": 120,
            "frequency": 1,
            "is_pleasant": True,
            "reward": "солнечный свет"
        }

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.pleasant_habit.pk}),
            data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['У приятной привычки не может быть вознаграждения или связанной привычки.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_reward_and_relate_validator(self):
        data = {
            "eta": 120,
            "frequency": 1,
            "is_pleasant": False,
            "reward": "силушка богатырская",
            "related_habit": self.pleasant_habit.pk
        }

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            reverse('habit:update_habit', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Нельзя одновременно выбрать связанную привычку и вознаграждение.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )