from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from school.models.school_model import SchoolModel
from school.forms.school_forms import SchoolForm


def list_school(request):
    school = SchoolModel.objects.filter(status=True)
    context = {
        'schools': school
    }
    return render(request, "listSchool.html", context)


def create_school(request):
    context = {
        'title': 'Ajouter une Ecole',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Ecole',
    }

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


def delete_school(request):
    school = get_object_or_404(SchoolModel, id=id)
    # school.delete()
    school.status = False
    school.save()
    return redirect('school:list_school')
