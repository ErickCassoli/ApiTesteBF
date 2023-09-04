from django.urls import path
from .views import UserView, UserLoginView

urlpatterns = [
    path('register/', UserView.as_view(), name='register'),
    path('auth/', UserLoginView.as_view(), name='register'),
]
