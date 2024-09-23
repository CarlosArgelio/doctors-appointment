from django.urls import path

from patients.views import ListPatients, DetailPatient

urlpatterns = [
    path("/", ListPatients.as_view()),
    path("/<int:pk>/", DetailPatient.as_view()),
]
