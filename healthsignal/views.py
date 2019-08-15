from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model # If used custom user model

from users.models import CustomToken


class GetData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        For testing so far
        :param request:
        :param format:
        :return:
        """
        return Response('Get valid data')

