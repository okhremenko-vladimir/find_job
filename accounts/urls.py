from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import MyLoginView, register

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
