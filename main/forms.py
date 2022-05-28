from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = '__all__'
        exclude = ('date_created', 'enrolment_status',)

        widgets = {
            'exam_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format: LastName, FirstName MiddleName'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'e.g., stsm@gmail.com'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control'}),
            'high_school': forms.TextInput(attrs={'class': 'form-control'}),
            'school_address': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'steward_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format: LastName, FirstName MiddleName'}),
            'steward_sex': forms.Select(attrs={'class': 'form-control'}),
            'steward_relationship': forms.Select(attrs={'class': 'form-control'}),
            'steward_contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'steward_email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'e.g., stsm@gmail.com'}),
            'steward_country': forms.TextInput(attrs={'class': 'form-control'}),
            'steward_city': forms.TextInput(attrs={'class': 'form-control'}),
            'steward_home_address': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., BS - Legal Management'}),
            'if_transferee': forms.CheckboxInput(attrs={"id": "chkPan", "onclick": "EnableDisableTextBox(this)"}),
            'uni_name': forms.TextInput(attrs={'class': 'form-control'}),
            'uni_country': forms.TextInput(attrs={'class': 'form-control'}),
            'uni_city': forms.TextInput(attrs={'class': 'form-control'}),
            'uni_address': forms.TextInput(attrs={'class': 'form-control'}),
            'uni_college': forms.TextInput(attrs={'class': 'form-control'}),
            'uni_course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., BS - Legal Management'}),
            'uni_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'uni_reason': forms.Textarea(attrs={'class': 'form-control'}),
        }
