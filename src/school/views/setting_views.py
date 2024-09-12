from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from urllib import request
from school.models.app_settings_model import AppSettingsModel
from school.forms.setting_forms import SettingForms
from school.models.app_settings_model import AppSettingsModel
from school.models.school_model import SchoolModel

@login_required(login_url='dashboard:sign_in')
def list_settings(request):
    setting = AppSettingsModel.objects.all()
    return render(request, 'setting/list.html', {'setting': setting})


def create_settings(request):
    school = SchoolModel.objects.all()
    setting = AppSettingsModel.objects.all()
    if setting:
        return redirect('school:school-create')

    if request.method == 'POST':
        form = SettingForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school:setting-list')
        else:
            print('erreur')
    else:
        form = SettingForms()
        context = {'form': form}
    return render(request, "setting/forms.html", context)

@login_required(login_url='dashboard:sign_in')
def update_settings(request, id):
    setting = AppSettingsModel.objects.get(id=id)
    if request.method == 'POST':
        form = SettingForms(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('list_settings')
        else:
            messages.error(request, 'erreur')
    else:
        form = SettingForms(instance=setting)
        context = {'form': form}
    return render(request, 'setting/forms.html', context)

@login_required(login_url='dashboard:sign_in')
def delete_settings(request, id):
    setting = AppSettingsModel.objects.get(id=id)
    if request.method == 'POST':
        #setting.delete()
        setting.status = False
        return redirect('list-school')
