from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.apps import UsersConfig
from apps.users.views import UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='user_list'),

    # paths to get a token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
