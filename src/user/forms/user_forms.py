from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models.user_model import UserModel
from django import forms


class UserForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'