from django.urls import path
from base.views.address_views import create_adress, list_adress, delete_adress, update_adress

app_name = 'address'
urlpatterns = [
    path('', list_adress, name='list-adress'),
    path('create_adress/', create_adress, name='create-adress'),
    path('update_adress/<int:id>', update_adress, name='update-adress'),
    path('delete_adress/<int:id>', delete_adress, name='delete-adress'),
]