from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.forms.absence_forms import AbsenceForm
from student.models.absence_model import AbsenceModel

@login_required(login_url='dashboard:sign_in')
def list_absence(request):
    absence = AbsenceModel.objects.filter(status=True)

    context = {
        'absence': absence
    }
    return render(request, "absence/list_absence.html", context)

@login_required(login_url='dashboard:sign_in')
def create_absence(request):
    context = {
        'title': 'Ajouter une Absence',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Absence',
    }

    if request.method == "POST":
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("absence:list_absence")
        else:
            print('erreur')
    else:
        form = AbsenceForm()
    context['form'] = form

    return render(request, "absence/form_absence.html", context)

@login_required(login_url='dashboard:sign_in')
def update_absence(request, id):
    absence = AbsenceModel.objects.get(id=id)
    context = {
        'title': 'Modifier l\'Absence',
        'submit_value': 'Modifier',
        'h1': 'Modifier Absence',
    }
    if request.method == "POST":
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect("absence:list_absence")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    form = AbsenceForm(instance=absence)
    context['form'] = form

    return render(request, "absence/form_absence.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_absence(request, id):
    absence = get_object_or_404(AbsenceModel, id=id)
    # absence.delete()
    absence.status = False
    absence.save()
    return redirect('absence:list_absence')



