from django import forms
from .models import Student

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'guardian_name', 'phone_number',  'student_id',  'village', 'ward', 'county',
                  'shelter', 'primary_school', 'secondary_school', 'tertially_school', 'date_of_adm', 'duration', 
                  'lever', 'scholarship_npf', 'scholarship_other', 'date_of_graduation','cohort','date_of_birth','profile_photo']
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class courseForm(forms.ModelForm):
    class Meta:
        fields = ['course_name','sem_period']
    