from django import forms
from .models import Appointment
from django.utils import timezone 


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {
            "appointment_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "appointment_time": forms.TimeInput(
                attrs={"type": "time"}
            ),
            "reason": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Reason for your visit (optional)"
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")

        if appointment_date and appointment_time:
            now = timezone.localtime()

            if appointment_date < now.date():
                self.add_error(
                    "appointment_date",
                    "You cannot book an appointment in the past."
                )

            elif (
                appointment_date == now.date()
                and appointment_time <= now.time().replace(tzinfo=None)
            ):
                self.add_error(
                    "appointment_time",
                    "Please select a future time."
                )

        return cleaned_data