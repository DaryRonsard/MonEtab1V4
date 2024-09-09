from django.shortcuts import render
from django.db import models
from django.shortcuts import render, redirect
from base.forms.forms_address import AddressForm
from base.models.address_model import AddressModel
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.


def list_adress(request):

    adress_list = AddressModel.objects.filter(status=True)

    context = {
        'adresses': adress_list
    }
    return render(request, "list.html", context)


def create_adress(request):
    context = {
        'title': 'Ajouter une Adresse',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Adresse',
    }

    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("address:list-adress")
        else:
            print('erreur')
    else:
        form = AddressForm()
    context['form'] = form

    return render(request, "form.html", context)



    adress_form = AddressForm(instance=adress)
    context['form'] = adress_form

    return render(request, "form.html", context)


def delete_adress(request, id):
    adress = get_object_or_404(AddressModel, id=id)
    # adress.delete()
    adress.status = False
    adress.save()
    return redirect('adress:list-adress')


def update_adress(request, id):
    adress = get_object_or_404(AddressModel, id=id)
    if request.method == 'POST':
        adress.status = False
        adress.save()
        print('adress')
        return redirect('address:list-adress')
