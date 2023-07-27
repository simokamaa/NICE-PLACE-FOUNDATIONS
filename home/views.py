from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,Course
from .forms import studentForm,courseForm
#from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'dashboard/files/index.html')

def admission(request):
    form=studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
       
        context = {'form':form}
        
    return render(request,'dashboard/files/Admission.html')

def courses(request):
    if request.method == 'POST':
        form = courseForm(request.POST,request.FILES )
    return render(request, 'dashboard/files/courses.html')

def clearance(request,pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'dashboard/files/clearance.html')

def user(request):
    return render(request, 'dashboard/files/user.html')

def update(request,pk):
    student = get_object_or_404(Student, pk=pk)


def report(request):
    students = Student.objects.all()
    return render(request,'dashboard/files/report.html',{'students' :students})

def rtl(request):
    return render(request,'dashboard/files/rtl.html')

def courses_view(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'dashboard/files/courses_view.html', context)

def generate_pdf(request,student):
    student=Student.objects.all()
    
    #creating a new pdf
    response = HttpResponse(content_type = 'application/pdf')
    response['content_Disposition '] = 'attachment; filename="student_report.pdf"  '
    
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
    
    