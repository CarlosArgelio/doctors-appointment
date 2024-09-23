from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from doctors.models import Doctor
from patients.models import Patient


class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            contact_number="1234567890",
            email="test@mail.com",
            address="123 Test St",
            medical_history="Test history",
        )
        self.doctor = Doctor.objects.create(
            first_name="John",
            last_name="Doe",
            qualification="MD",
            contact_number="1234567890",
            email="doctor@mail.com",
            address="123 Test St",
            biography="Test bio",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_should_return_status_code_200_when_get_list(self):
        url = reverse("doctor-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
