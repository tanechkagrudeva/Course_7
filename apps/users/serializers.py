from os import getenv

import requests
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    Fields:
    - email (EmailField): Email address of the user. Used for authentication.
    - chat_id (CharField): Telegram chat id for sending messages. Can be NULL.
    - avatar (ImageField): Avatar image of the user.
    """
    chat_id = serializers.SerializerMethodField()

    def get_chat_id(self, user):
        """ get chat id for telegram """
        response = requests.request("GET", f'https://api.telegram.org/bot{getenv("TG_API_KEY")}/getUpdates')
        data = response.json()
        chat_id = data['result'][0]['message']['chat']['id']
        return chat_id

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """ setting password """
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)