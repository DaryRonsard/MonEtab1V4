from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.models.role_user_model import RoleUserModel
from user.forms.role_forms import RoleUserForms

@login_required(login_url='dashboard:sign_in')
def list_role_user(request):
    role = RoleUserModel.objects.all()
    context = {'role': role}
    return render(request, 'role/list.html', context)

@login_required(login_url='dashboard:sign_in')
def create_role_user(request):
    form = RoleUserForms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user_role:list-role')
        else:
            print('erreur')
    context = {'form': form}
    return render(request, 'role/forms.html', context)

@login_required(login_url='dashboard:sign_in')
def update_role_user(request, id):
    role_user = RoleUserModel.objects.get(id=id)
    context = {
        'title': 'Modifier le Rôle de l\'Utilisateur',
        'submit_value': 'Modifier',
        'h1': 'Modifier Rôle Utilisateur',
    }
    if request.method == "POST":
        role_user_form = RoleUserForms(request.POST, instance=role_user)
        if role_user_form.is_valid():
            role_user_form.save()
            return redirect("role_user:list_role_user")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    role_user_form = RoleUserForms(instance=role_user)
    context['form'] = role_user_form

    return render(request, "role/forms.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_role_user(request, id):
    role_user = get_object_or_404(RoleUserModel, id=id)
    # role_user.delete()
    role_user.status = False
    role_user.save()
    return redirect('role_user:list_role_user')
