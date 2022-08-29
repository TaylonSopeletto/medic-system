from rest_framework import serializers
from medic.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'taxNumber', 'registrationNumber']