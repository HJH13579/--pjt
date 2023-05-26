# from django.shortcuts import render, get_object_or_404

# # Create your views here.
# from rest_framework import status, viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response

from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# 로그인 뷰에 대해서는 django-rest-framework-simplejwt 라이브러리를 활용하거나 custom 로그인 뷰를 구현해야 할 수 있습니다.

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
