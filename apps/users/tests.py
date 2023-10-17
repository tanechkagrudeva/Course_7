from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class UserTestCase(APITestCase):

    def test_user_create(self):
        url = reverse('users:user_create')
        data = {"email": "test@email.com", "password": "123qwe"}

        response = self.client.post(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.all().count(),
            1
        )

        self.assertTrue(
            User.objects.get(),
        )
