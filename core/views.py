from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer, RegisterSerializer

# Login Authentication
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id})

# User Registration
class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_201_CREATED)

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
