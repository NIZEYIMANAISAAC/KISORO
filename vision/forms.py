from django import forms
from .models import AdmissionApplication


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['applicant_name', 'student_name', 'date_of_birth', 'program', 'email', 'phone', 'address', 'document']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }