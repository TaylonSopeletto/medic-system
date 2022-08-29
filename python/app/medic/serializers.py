from rest_framework import serializers
from medic.models import Patient, Doctor
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'taxNumber', 'registrationNumber']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'taxNumber', 'registrationNumber', 'specialization', 'salary']


class UserSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']