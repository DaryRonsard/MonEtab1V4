from django import forms
from school.models.school_model import SchoolModel


class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolModel
        fields = ['app', 'name', 'url_logo']