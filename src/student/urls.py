from django.urls import path

from student.views.views_student import list_students,create_student,update_student, delete_student
from student.views.views_student_cards import create_cards, update_cards, list_cards, delete_cards
from student.views.views_absence import create_absence, list_absence, delete_absence, update_absence

app_name = 'student'
urlpatterns = [
    #student
    path('', list_students, name='list-students'),
    path('create_student/', create_student, name='create-student'),
    path('update_student/', update_student, name='update-student'),
    path('delete_student/', delete_student, name='delete-student'),


    #absence
    path("list_absence/", list_absence, name='list-absence'),
    path('create_absence/', create_absence, name='create-absence'),
    path('list_absence/<int:id>', list_absence, name='list-absence'),
    path('delete_absence/<int:id>', delete_absence, name='delete-absence'),


    #cards
    path('list_cards/', list_absence, name='list-absence'),
    path('create_cards/', create_absence, name='create-absence'),
    path('update_cards/<int:id>', update_absence, name='update-absence'),
    path('delete_cards/<int:id>', delete_cards, name='delete-cards'),
]