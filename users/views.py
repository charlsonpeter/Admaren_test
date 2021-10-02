from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from .serializers import *
import requests
import json


# User Register API
class RegisterApi(generics.GenericAPIView):
    """
    User register API
    """
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
        "message": "User Created Successfully."})


class UserLogin(APIView):
    """
    User Login API
    """
    permission_classes=[AllowAny,]
    def post(self, request):
        try:
            str_username= request.data['username']
            str_password=request.data['password']
            user = authenticate(request, username=str_username, password=str_password)
            if user:
                login(request, user)
                token_json = requests.post(request.scheme+'://'+request.get_host()+'/api-token-auth/',{'username':str_username,'password':str_password})
                token = json.loads(token_json._content.decode("utf-8"))['token']
                user_details = {
                    "username": user.username,
                    "email": user.email
                }
                return Response({'token': token, "user_details": user_details,"message": "Logged in sucessfully"},status=status.HTTP_200_OK)
            else:
                return Response({"message": "Authentication Failed"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'reason':str(e), 'message':'Somthing went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RefreshToken(APIView):
    """
    Refresh Token
    """
    permission_classes=[IsAuthenticated,]
    def post(self, request):
        if request.data.get('token'):
            token_json = requests.post(request.scheme+'://'+request.get_host()+'/api-token-refresh/', {'token':request.data.get('token')})
            return Response(token_json.json(), status=status.HTTP_200_OK)
        else:
            return Response({"message": "Authentication Failed"},status=status.HTTP_404_NOT_FOUND)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/user/login')
