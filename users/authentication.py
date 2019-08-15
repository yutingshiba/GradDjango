from datetime import timedelta

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from django.conf import settings

from .models import CustomToken


def is_token_expired(token):
    """Expire if lastused > TOKEN_EXPIRED_AFTER_SECONDS or created > TOKEN_CREATED_TOO_LONG"""
    return (timezone.now() - token.lastused) > timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) or \
           (timezone.now() - token.created) > timedelta(seconds=settings.TOKEN_CREATED_TOO_LONG)


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    def authenticate_credentials(self, key):
        try:
            token = CustomToken.objects.get(key=key)
        except CustomToken.DoesNotExist:
            raise AuthenticationFailed("Invalid Token.")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active.")

        if is_token_expired(token):
            raise AuthenticationFailed("The Token is expired. Please login again.")
        return token.user, token
