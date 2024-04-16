from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# login Authenticate
class Login(ObtainAuthToken):
    def post(self, request, *args,**kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id": user.id})
    