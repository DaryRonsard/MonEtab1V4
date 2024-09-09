from django.contrib import messages
from django.shortcuts import render, redirect
from urllib import request
from school.forms.setting_forms import SettingForms
from school.models.app_settings_model import AppSettingsModel


def list_settings(request):
    setting = AppSettingsModel.objects.get()
    return render(request, 'setting/forms.html', {'setting': setting})


def create_settings(request):
    if request.method == 'POST':
        form = SettingForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_settings')
        else:
            print('erreur')
    else:
        form = SettingForms()
        context = {'form': form}
    return render(request, "setting/list.html", context)


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


def delete_settings(request, id):
    setting = AppSettingsModel.objects.get(id=id)
    if request.method == 'POST':
        #setting.delete()
        setting.status = False
        return redirect('list-school')
