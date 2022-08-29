from rest_framework import serializers
from medic.models import Patient, Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'taxNumber', 'registrationNumber']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'taxNumber', 'registrationNumber', 'specialization', 'salary']