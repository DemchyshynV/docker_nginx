from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CustomTokenRefreshView, CreateInviteView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', CustomTokenRefreshView.as_view()),
    path('/invites', CreateInviteView.as_view())
]
