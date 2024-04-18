from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer, RegisterSerializer

# login Authenticate
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id})

# User Registration
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Pass the user instance, not just the user_id
            profile_serializer = ProfileSerializer(data={'user': user.id, 'other_field': 'value'})
            if profile_serializer.is_valid():
                profile_serializer.save(user=user)  # Pass the user instance to save method
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_201_CREATED)
            else:
                user.delete()  # Delete the user if profile creation fails
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

