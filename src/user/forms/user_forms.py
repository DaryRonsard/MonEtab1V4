from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models.user_model import UserModel
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'school', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }