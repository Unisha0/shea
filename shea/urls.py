# shea/urls.py
from django.urls import path
from . import views
from .views import hospital_dashboard,patient_dashboard
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('hospital/dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
]

