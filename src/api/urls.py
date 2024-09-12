from django.urls import path
from api.apiviews import student_apiviews
from api.apiviews.student_apiviews import student_list

urlpatterns = [
    path('', student_list),
]