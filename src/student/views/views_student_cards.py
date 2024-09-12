from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.forms.student_cards_forms import StudentCardForm
from student.models.student_cards_model import StudentCardsModel

@login_required(login_url='dashboard:sign_in')
def list_cards(request):
    cards = StudentCardsModel.objects.filter(status=True)

    context = {
        'cards': cards
    }
    return render(request, "cards/list_student.html", context)

@login_required(login_url='dashboard:sign_in')
def create_cards(request):
    context = {
        'title': 'Ajouter une Carte élève',
        'submit_value': 'Ajouter',
        'h1': 'Nouvelle Carte',
    }

    if request.method == "POST":
        form = StudentCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_cards:list_student_card")
        else:
            print('erreur')
    else:
        form = StudentCardForm()
    context['form'] = form

    return render(request, "cards/form_student.html", context)

@login_required(login_url='dashboard:sign_in')
def update_cards(request, id):
    cards = StudentCardsModel.objects.get(id=id)
    context = {
        'title': 'Modifier la carte',
        'submit_value': 'Modifier',
        'h1': 'Modifier Carte Eleve',
    }
    if request.method == "POST":
        form = StudentCardForm(request.POST, instance=cards)
        if form.is_valid():
            form.save()
            return redirect("student_cards:list_student_card")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    form = StudentCardForm(instance=cards)
    context['form'] = form

    return render(request, "cards/form_student.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_cards(request, id):
    student_card = get_object_or_404(StudentCardsModel, id=id)
    # student_card.delete()
    student_card.status = False
    student_card.save()
    return redirect('student_cards:list_student_card')