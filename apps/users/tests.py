from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class UserTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/users/views"""

    def setUp(self) -> None:
        self.url = '/users/user/create/'
        self.data = {
            'username': 'test',
            'password': 'test',
            'telegram': 'test'
        }

    def test_1_create_user(self):
        """User creation testing """

        response = self.client.post(f'{self.url}', data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(User.objects.all().count(), 1)
