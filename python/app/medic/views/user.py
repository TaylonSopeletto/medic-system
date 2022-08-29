from django.shortcuts import render
from medic import serializers
from rest_framework import generics
from medic.models import Patient
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class Register(generics.GenericAPIView):

    serializer_class = serializers.UserSerializerRegister

    def post(self, request):
        data = request.data
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'])
        user.save()
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)