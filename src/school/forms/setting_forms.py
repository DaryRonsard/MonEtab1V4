from django import forms
from school.models.app_settings_model import AppSettingsModel


class SettingForms(forms.ModelForm):
    class Meta:
        model = AppSettingsModel
        fields = ['smtp_server', 'smtp_port', 'smtp_username', 'smtp_password']
