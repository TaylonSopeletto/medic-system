from django.urls import path
from medic import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

    path('authenticate/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authenticate/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticate/register/', views.Register.as_view()),

    path('patients/', views.PatientList.as_view() ),
    path('patients/<int:pk>', views.PatientDetail.as_view()),

    path('doctors/', views.DoctorList.as_view() ),
    path('doctors/<int:pk>', views.DoctorDetail.as_view()),
]