from django import forms
from .models import Day

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['alias', 'date_time', 'activities', 'workout', 'academic', 'sr', 'economics']