from django import forms
from teacher.models.teacher_model import TeacherModel


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        exclude = ['status',]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
