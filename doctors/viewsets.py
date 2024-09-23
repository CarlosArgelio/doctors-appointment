from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment

from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)
from .permissions import IsDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(detail=True, methods=["post"], url_path="set-on-vacation")
    def set_on_vacation(self, request, pk=None):
        """
        Set the doctor on vacation.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})

    @action(detail=True, methods=["post"], url_path="set-off-vacation")
    def set_off_vacation(self, request, pk=None):
        """
        Set the doctor off vacation.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})

    @action(
        detail=True, methods=["POST", "GET"], serializer_class=AppointmentSerializer
    )
    def appointments(self, request, pk=None):
        doctor = self.get_object()
        data = request.data.copy()
        data["doctor"] = doctor.id

        if request.method == "POST":
            # Create an appointment for the doctor
            serializer = AppointmentSerializer(data=data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == "GET":
            # Get all appointments for the doctor
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
