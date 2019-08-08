from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model  # If used custom user model

from .serializers import UserSerializer

UserModel = get_user_model()
# Create your views here.
class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


class GetTokenView(APIView):

    def get(self, request):
        uname = request.query_params.get('uname', '')
        try:
            user = UserModel.objects.get(username=uname)
        except UserModel.DoesNotExist:
            return Response('User not exist')
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)
