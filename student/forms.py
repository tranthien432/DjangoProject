from django import forms
from student.models import Students, ClassST


class ClassForm(forms.ModelForm):
    class Meta:
        model = ClassST
        fields = "__all__"


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
