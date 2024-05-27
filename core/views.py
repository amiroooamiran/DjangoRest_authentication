from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile
from .serializers import ProfileSerializer,RegisterSerializer, EmailVerificationSerializer, RestePasswordSerializer
from .producer import publish
from .utils import Util

# Login Authentication
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        publish()
        return Response({"token": token.key, "user_id": user.id})

class ResetPassword(generics.GenericAPIView):
    serializer_class = RestePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)

# User Registration
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = [JSONRenderer]  # Add JSONRenderer as the renderer class

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        email_body = (
            f"Hi {user.username},\n"
            f"Welcome To Authentication Project\n"
        )
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Welcome',
        }

        Util.send_email(data)  # Assuming send_email function is defined in Util module
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# verfication
class VerifyEmail(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer

    def get(self):
        pass

# User Profile
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        user = self.request.user
        # Attempt to retrieve the profile associated with the user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            # If profile doesn't exist, create a new one
            profile = Profile.objects.create(user=user)
        return profile
