from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("doctors/",views.doctor_list, name="doctor_list"),
    path("doctors/<int:pk>/",views.doctor_detail, name="doctor_detail"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("doctors/<int:doctor_id>/book/", views.book_appointment, name="book_appointment",),
    path("appointments/", views.my_appointments, name="my_appointments",),
    path("appointments/<int:appointment_id>/cancel/", views.cancel_appointment, name="cancel_appointment",),
]