from django.shortcuts import render, get_object_or_404
from .models import Doctor , Appointment
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required   
from .forms import AppointmentForm

def home(request):
    return render(request, "doctors/home.html")


def doctor_list(request):
    doctors = Doctor.objects.filter(available=True)

    search_query = request.GET.get("search", "")
    specialization = request.GET.get("specialization", "")

    if search_query:
        doctors = doctors.filter(name__icontains=search_query)

    if specialization:
        doctors = doctors.filter(
            specialization__iexact=specialization
        )

    specializations = (
        Doctor.objects.filter(available=True)
        .values_list("specialization", flat=True)
        .distinct()
    )

    context = {
        "doctors": doctors,
        "search_query": search_query,
        "selected_specialization": specialization,
        "specializations": specializations,
    }

    return render(request, "doctors/doctor_list.html", context)

def doctor_detail(request, pk):
    doctor = get_object_or_404(
        Doctor,
        pk=pk,
        available=True
    )

    return render(
        request,
        "doctors/doctor_detail.html",
        {"doctor": doctor}
    )

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(
        request,
        "doctors/register.html",
        {"form": form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "doctors/login.html",
        {"form": form}
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)

    return redirect("home")

@login_required
@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment_date = form.cleaned_data["appointment_date"]
            appointment_time = form.cleaned_data["appointment_time"]

            already_booked = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            ).exclude(
                status="Cancelled"
            ).exists()

            if already_booked:
                form.add_error(
                    None,
                    "This doctor already has a booking at that time. "
                    "Please choose another time."
                )
            else:
                appointment = form.save(commit=False)
                appointment.patient = request.user
                appointment.doctor = doctor
                appointment.save()

                messages.success(
                    request,
                    "Your appointment request was submitted successfully!"
                )

                return redirect("my_appointments")
    else:
        form = AppointmentForm()

    return render(
        request,
        "doctors/book_appointment.html",
        {"doctor": doctor, "form": form}
    )

def my_appointments(request):
    appointments = Appointment.objects.filter(
        patient=request.user
    ).order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "doctors/my_appointments.html",
        {"appointments": appointments}
    )

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        patient=request.user
    )

    if appointment.status == "Pending":
        appointment.status = "Cancelled"
        appointment.save(update_fields=["status"])

        messages.success(
            request,
            "Your appointment has been cancelled successfully."
        )
    else:
        messages.error(
            request,
            "Only pending appointments can be cancelled."
        )

    return redirect("my_appointments")