from django.db import models

class manager(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    guardian_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20, unique=True)
    village = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    shelter = models.CharField(max_length=100)
    primary_school = models.CharField(max_length=20)
    secondary_school = models.CharField(max_length=20)
    tertially_school = models.CharField(max_length=200)
    date_of_adm = models.DateTimeField()
    duration = models.IntegerField()
    lever = models.IntegerField()
    scholarship_npf = models.BooleanField()
    scholarship_other = models.BooleanField()
    date_of_graduation = models.DateTimeField()
    cohort = models.IntegerField()
    date_of_birth = models.DateTimeField()
    profile_photo = models.ImageField(upload_to='student_profile_photos/', null=True, blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    sem_period = models.CharField(max_length=50)
    