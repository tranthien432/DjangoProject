from django.shortcuts import render, redirect
from .models import Students, ClassST
from student.forms import StudentsForm, ClassForm



def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html', {'title': 'about'})


def profile(request):
    return render(request, 'profile/profile.html', {'title': 'profile'})


def login(request):
    return render(request, 'account/login.html', {'title': 'login'})


def createstudent(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        # print(form)
        if form.is_valid():
            print(form)
            try:
                form.save()
                return redirect('student-list')
            except:
                pass

    else:
        form = StudentsForm()
    students = Students.objects.all()
    idClass = ClassST.objects.all()
    return render(request, 'student/student.html', {'forms': form, 'students': students, 'classIds': idClass})


def createclass(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('class-list')
            except:
                pass

    else:
        form = ClassForm()
    classstudent = ClassST.objects.all()
    return render(request, 'studentclass/studentclass.html', {'forms': form, 'studentclass': classstudent})


def deleteclass(request, id):
    studentclass = ClassST.objects.get(id=id)
    studentclass.delete()
    return redirect('class-list')


def editclass(request, id):
    studentclass = ClassST.objects.get(id=id)
    forms = ClassForm()
    return render(request, 'studentclass/editclass.html', {'studentclass': studentclass, 'form': forms})
