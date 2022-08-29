from django.shortcuts import render
from medic import serializers
from rest_framework import generics
from medic.models import Doctor
from rest_framework.response import Response
from rest_framework import status

class DoctorDetail(generics.GenericAPIView):

    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

    def get(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        serializer =  serializers.DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        doctor.name = request.data["name"]
        doctor.taxNumber = request.data["taxNumber"]
        doctor.registrationNumber = request.data["registrationNumber"]

        serializer = serializers.DoctorSerializer(doctor)
        doctor.save()
        return Response(serializer.data)


class DoctorList(generics.GenericAPIView):
    
    serializer_class = serializers.DoctorSerializer
   
    def get(self, request, format=None):

        doctors = Doctor.objects.all()
        serializer = serializers.DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
    
        doctor = serializers.DoctorSerializer(data=request.data)

        if doctor.is_valid():
            doctor.save()
            return Response(doctor.data, status=status.HTTP_201_CREATED)
        return Response(doctor.data, status.HTTP_400_BAD_REQUEST)

    