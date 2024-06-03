from django.urls import path

from .views import Login, ProfileView, RegisterView, VerifyEmail, ResetPassword

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]
