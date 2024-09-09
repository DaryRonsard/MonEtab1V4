from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import render, redirect

from user.models import UserModel, RoleUserModel
from user.forms.user_forms import UserForms


# Create your views here.

def list_user(request):
    users = UserModel.objects.all()

    number_user = users.count()
    context = {
        'users': users,
        'total': number_user,

    }
    return render(request, "listUser.html", context)


def create_user(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_role:create-user')
    roles = RoleUserModel.objects.all()
    print(roles)
    form = UserForms()
    context = {
        'form': form,
        'roles': roles,
    }
    return render(request, 'formUser.html', context)


def update_user(request, id):
    pass


def delete_user(request, id):
    pass
