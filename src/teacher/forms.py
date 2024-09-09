from django import forms
from .models.teacher_model import TeacherModel


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        exclude = ['gender', 'url_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
