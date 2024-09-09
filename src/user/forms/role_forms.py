from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models.role_user_model import RoleUserModel
from django import forms


class RoleUserForms(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = ['role']
