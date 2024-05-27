from django.urls import path

from .views import Login, ProfileView, RegisterView, VerifyEmail, ResetPassword

urlpatterns = [
    path('register/', RegisterView.as_view({'post' : 'post'}), name='register'),
    path('login/', Login.as_view({'post' : 'post'}), name='login'),
    path('profile/', ProfileView.as_view({'get' : 'get_object'}), name='profile'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('reset_password/', ResetPassword.as_view({'put' : 'post'}), name="reset_password")
]
