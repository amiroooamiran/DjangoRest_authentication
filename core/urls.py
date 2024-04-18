from django.urls import path

from .views import Login, ProfileView, Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')
]
