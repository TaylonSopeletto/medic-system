from django.urls import path
from medic import views

urlpatterns = [
    path('patients/', views.PatientList.as_view() ),
    path('patients/<int:pk>', views.PatientDetail.as_view()),
]