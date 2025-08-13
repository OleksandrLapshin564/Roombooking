from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["guest_name", "check_in", "check_out"]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError("Check-out date must be after check-in date.")

        # Check for existing reservations for the same room if there is access to the instance and room
        if hasattr(self, 'instance') and self.instance.pk is not None:
            # To update your booking - exclude yourself
            existing_bookings = Booking.objects.filter(
                room=self.instance.room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exclude(pk=self.instance.pk)
        else:
            # For a new booking
            room = getattr(self.instance, 'room', None)
            # room must be passed in instance to the form
            if room is not None:
                existing_bookings = Booking.objects.filter(
                    room=room,
                    check_in__lt=check_out,
                    check_out__gt=check_in
                )
            else:
                existing_bookings = Booking.objects.none()

        if existing_bookings.exists():
            raise forms.ValidationError("This room is already booked for the selected dates.")

        return cleaned_data
