from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)
    guardian_name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='student_profile_photos/', null=True, blank=True)


#Create a StudentForm class in the student app's forms.py file that represents the form used to create and update Student objects. For example:

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'guardian_name', 'village', 'ward', 'county', 'profile_photo']
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }

#views.py
from django.shortcuts import render, redirect, get_object_or_404
from . models import Student
from . forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request

#login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'authentication/login.html')


#urls
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
]


{% extends 'base.html' %}

{% block content %}
    <h2>Login</h2>
    {% if error_message %}
        <p>{{ error_message }}</p>
    {% endif %}
    <form method="post">
        {% csrf_token %}
        <div>
            <label for="username">Username:</label>
            <input type="text" name="username" id="username">
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password">
        </div>
        <button type="submit">Login</button>
    </form>
{% endblock %}

#homepage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'authentication/home.html')

#view function for generating pdf
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_pdf(request, student_id):
    # Retrieve the student object with the specified ID
    student = Student.objects.get(id=student_id)

    # Create a new PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_report.pdf"'
    p = canvas.Canvas(response)

    # Write some text to the PDF
    p.drawString(100, 750, "Student Report")
    p.drawString(100, 700, f"Name: {student.firstname} {student.lastname}")
    p.drawString(100, 650, f"Student ID: {student.student_id}")
    p.drawString(100, 600, f"Guardian Name: {student.guardian_name}")
    p.drawString(100, 550, f"Village: {student.village}")
    p.drawString(100, 500, f"Ward: {student.ward}")
    p.drawString(100, 450, f"County: {student.county}")

    # Save the PDF and return it as an HTTP response
    p.showPage()
    p.save()
    return response

#url
from django.urls import path
from . import views

urlpatterns = [
    path('students/<int:student_id>/pdf/', views.generate_pdf, name='generate_pdf'),
]

#btn
<a href="{% url 'generate_pdf' student.id %}">Generate PDF</a>

