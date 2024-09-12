from django import forms
from student.models.student_model import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        exclude = ['gender', 'url_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }