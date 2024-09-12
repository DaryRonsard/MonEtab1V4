from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from school.models.school_model import SchoolModel
from school.models.app_settings_model import AppSettingsModel
from user.models import UserModel, RoleUserModel
from user.forms.user_forms import UserForms


# Create your views here.
@login_required(login_url='dashboard:sign_in')
def list_user(request):
    users = UserModel.objects.all()

    number_user = users.count()
    context = {
        'users': users,
        'total': number_user,

    }
    return render(request, "listUser.html", context)


@login_required(login_url='dashboard:sign_in')
def create_user(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        form = UserForms(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.set_password(password)
            forms.save()
            return redirect('user_role:list-user')
    roles = RoleUserModel.objects.all()
    print(roles)
    form = UserForms()
    context = {
        'form': form,
        'roles': roles,
    }
    return render(request, 'formUser.html', context)


@login_required(login_url='dashboard:sign_in')
def update_user(request, id):
    pass


@login_required(login_url='dashboard:sign_in')
def delete_user(request, id):
    pass


def connexion(request):
    setting = AppSettingsModel.objects.all()
    school = SchoolModel.objects.all()
    if not setting:
        return redirect('school:setting-create')
    if not school:
        return redirect('school:school-create')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        if not username and not password:
            print(username, password)
            messages.error('Error')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return redirect('dashboard:sign_in')
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    return render(request, 'connexion/connexion.html', )


@login_required(login_url='dashboard:sign_in')
def disconnect(request):
    logout(request)
    return redirect('dashboard:sign_in')
