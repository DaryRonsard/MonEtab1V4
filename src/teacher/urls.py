from django.urls import path

from teacher.views import list_teachers, create_teacher, update_teacher, delete_teacher

app_name = 'teacher'
urlpatterns = [
    path('', list_teachers, name='list-teachers'),
    path('create_teacher/', create_teacher, name='create-teacher'),
    path('update_teacher/<int:id>', update_teacher, name='update-teacher'),
    path('delete_teacher/<int:id>', delete_teacher, name='delete-teacher'),
]