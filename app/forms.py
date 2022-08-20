from django import forms

from .models import Child
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    
    class Meta():
        model = Attendance
        fields = ('date', 'child', 'attendance', 'reason')


class ResponForm(forms.ModelForm):
    
    class Meta():
        model = Attendance
        fields = ('respon',)

