from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
# Create your views here.


class UserCreateView(APIView):

    def post(self,request):
        email = request.data.get("email")
        existing_user = User.objects.get(email=email)
        # if user exist 
        if existing_user:
            return Response({"message":"user already exist"})
        # if user does not exist
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    
class LoginUserView(APIView):

     def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        username = User.objects.get(name=username)
        # Authenticate the user
        Loginuser = authenticate(username=username, password=password)
        print(Loginuser)

        if Loginuser is not None:
            return Response({"message": "login successful"})
        else:
            return Response({"message": "login failed"}, status=400)