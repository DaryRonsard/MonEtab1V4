from django import forms
from base.models.address_model import AddressModel


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = '__all__'
