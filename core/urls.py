from django.urls import path
from .views import UserProfileView, DoctorListView, AppointmentCreateView, AppointmentListView

urlpatterns = [
    path('profile/', UserProfileView.as_view()),
    path('doctors/', DoctorListView.as_view()),
    path('appointments/create/', AppointmentCreateView.as_view()),
    path('appointments/', AppointmentListView.as_view()),  # same path but different HTTP methods
]
