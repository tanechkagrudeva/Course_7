from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """View to create a user.
       To create you need to enter username, password and telegram username.
       In case of the tests don't forget to change permissions."""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
