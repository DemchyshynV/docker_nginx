from django.urls import path
from .views import GetCurrentUserView

urlpatterns = [
    path('', GetCurrentUserView.as_view())
]
