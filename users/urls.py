from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('', UserListAPIView.as_view(), name='users'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("payments/", PaymentListAPIView.as_view(), name="payment-list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
]