from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from .serializers import UserSerializer
from .models import CustomToken

UserModel = get_user_model()


class SignUpView(CreateAPIView):
    """Create an user with given email and password."""

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


class LogInView(APIView):
    """Log in with email and password."""

    def get(self, request):
        email = request.query_params.get('email', '')
        password = request.query_params.get('password', None)
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response('Email does not exist.')
        if not user.check_password(password):
            return Response('Incorrect password.')

        # Always renew token after login
        token, created = CustomToken.objects.get_or_create(user=user)
        if not created:
            token.delete()
            token, created = CustomToken.objects.get_or_create(user=user)
            token.save()  # Update lastused field

        return Response('{};;;{}'.format(token.key, created))


class LogOutView(APIView):

    def get(self, request):
        if not isinstance(request.user, AnonymousUser):
            token, created = CustomToken.objects.get_or_create(user=request.user)
            token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
