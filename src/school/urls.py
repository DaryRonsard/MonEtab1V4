from django.urls import path
from school.views.school_views import create_school, list_school, update_school, delete_school
from school.views.setting_views import list_settings, create_settings, update_settings, delete_settings

app_name = 'school'
urlpatterns = [
    #school
    path('', list_school, name='list-school'),
    path('create_school/', create_school, name='school-create'),
    path('update_school/', update_school, name='school-update'),
    path('delete_school/', delete_school, name='school-delete'),


    #setting
    path('setting_list/', list_settings, name='setting-list'),
    path('setting_create/', create_settings, name='setting-create'),
    path('setting_update/', update_settings, name='setting-update'),
    path('setting_delete/', delete_settings, name='setting-delete'),
]