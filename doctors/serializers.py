from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_email(self, value):
        if "@example.com" in value:
            raise value

        raise serializers.ValidationError("Email is not from example.com domain")

    def validate(self, data):
        if len(data["contact_number"]) <= 10 and data["is_on_vacation"] == True:
            raise serializers.ValidationError("Invalid contact number")

        return super().validate(data)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"
