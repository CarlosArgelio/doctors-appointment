from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PatientSerializer
from .models import Patient


class ListPatients(ListAPIView, CreateAPIView):
    alloewd_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatient(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
