from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)  # return full details
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['user']
    
    def validate_appointment_date(self, value):
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value
