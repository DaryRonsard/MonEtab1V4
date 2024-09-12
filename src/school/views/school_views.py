from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from school.models.app_settings_model import AppSettingsModel
from school.models.school_model import SchoolModel
from school.forms.school_forms import SchoolForm

@login_required(login_url='dashboard:sign_in')
def list_school(request):
    school = SchoolModel.objects.filter(status=True)
    context = {
        'school': school
    }
    return render(request, "listSchool.html", context)


def create_school(request):
    context = {
        'title': 'Ajouter une Ecole',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Ecole',
    }
    setting = AppSettingsModel.objects.all()
    school = SchoolModel.objects.all()
    if school:
        return redirect('dashboard:sign_in')
    if not setting:
        return redirect('school:setting-create')
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("school:list-school")
        else:
            print('erreur')
    else:
        form = SchoolForm()
    context['form'] = form

    return render(request, "formsSchool.html", context)

@login_required(login_url='dashboard:sign_in')
def update_school(request):
    school = SchoolModel.objects.get(id=id)
    context = {
        'title': 'Modifier Ecole',
        'submit_value': 'Modifier',
        'h1': 'Modifier Ecole',
    }
    if request.method == "POST":
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return redirect("school:list-school")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    school_form = SchoolForm(instance=school)
    context['form'] = school_form

    return render(request, "formsSchool.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_school(request):
    school = get_object_or_404(SchoolModel, id=id)
    # school.delete()
    school.status = False
    school.save()
    return redirect('school:list_school')
