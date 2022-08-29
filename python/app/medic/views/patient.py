from django.shortcuts import render
from medic import serializers
from rest_framework import generics
from medic.models import Patient
from rest_framework.response import Response
from rest_framework import status

class PatientDetail(generics.GenericAPIView):

    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer

    def get(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        serializer =  serializers.PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        patient.name = request.data["name"]
        patient.taxNumber = request.data["taxNumber"]
        patient.registrationNumber = request.data["registrationNumber"]

        serializer = serializers.PatientSerializer(patient)
        patient.save()
        return Response(serializer.data)


class PatientList(generics.GenericAPIView):
    
    serializer_class = serializers.PatientSerializer
   
    def get(self, request, format=None):

        patients = Patient.objects.all()
        serializer = serializers.PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
    
        patient = serializers.PatientSerializer(data=request.data)

        if patient.is_valid():
            patient.save()
            return Response(patient.data, status=status.HTTP_201_CREATED)
        return Response(patient.data, status.HTTP_400_BAD_REQUEST)

    