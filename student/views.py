from django.shortcuts import render
from student.models import Students


def home(request):
    # return render(request, 'student/home.html')
    students = Students.objects.all()
    return render(request, 'student/home.html', {'students': students})


def about(request):
    return render(request, 'student/about.html', {'title': 'about'})
