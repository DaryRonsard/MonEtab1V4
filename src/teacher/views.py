from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.models.teacher_model import TeacherModel
from teacher.forms.teacher_forms import TeacherForm
from user.models.user_model import UserModel


#from user.forms.user_form import UserForm


# Create your views here.
@login_required(login_url='dashboard:sign_in')
def list_teachers(request):
    teacher = TeacherModel.objects.filter(status=True)

    context = {
        'teachers': teacher
    }
    return render(request, "listTeacher.html", context)

@login_required(login_url='dashboard:sign_in')
def create_teacher(request):
    context = {
        'title': 'Ajouter un Professeur',
        'submit_value': 'Ajouter',
        'h1': 'Nouveau Professeur',
    }

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            #teacher = form.save(commit=False)
            form.save()
            messages.success(request, 'Le professeur a été ajouté avec succès.')
            return redirect('teacher:list-teachers')
        else:
            print(form.errors)
    else:
        form = TeacherForm()
        # user_form = UserForm()
    context['form'] = form
    # context['forms'] = user_form

    return render(request, "formsTeacher.html", context)

@login_required(login_url='dashboard:sign_in')
def update_teacher(request, id):
    teacher = TeacherModel.objects.get(id=id)
    # user = get_object_or_404(UserModel, teacher=teacher)
    context = {
        'title': 'Modifier le professeur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Professeur',
    }
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        # user_form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # user_form.save()
            return redirect("teacher:list-teacher")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    form = TeacherForm(instance=teacher)
    # user_form = UserForm(instance=user)
    context['form'] = form
    # context['forms'] = user_form

    return render(request, "formsTeacher.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_teacher(request, id):
    teacher = get_object_or_404(TeacherModel, id=id)
    # teacher.delete()
    # user = get_object_or_404(UserModel, teacher=teacher)
    teacher.status = False
    teacher.active = False
    teacher.save()
    # user.is_active = False
    # user.save()
    return redirect('teacher:list-teacher')
