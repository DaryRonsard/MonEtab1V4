from django.urls import path, include
from user.views import user_views
from django.urls import path
from user.views.role_user_views import list_role_user , create_role_user, update_role_user, delete_role_user
from user.views.user_views import list_user, create_user, update_user, delete_user
#from user.views.role_user_views import list_role_user, update_role_user, create_role_user, delete_role_user



app_name = 'user_role'
urlpatterns = [
    # urls de users
    path('', list_user, name='list-user'),
    path('create_user/', create_user, name='create-user'),
    path('update_user/', update_user, name='update-user'),
    path('delete_user/', delete_user, name='delete-user'),


    #vues de role
    path('list_role_user/', list_role_user, name='list-role'),
    path('create_role/', create_role_user, name='create-role'),
    path('update_role/', update_role_user, name='update-role'),
    path('delete_role/', delete_role_user, name='delete-role'),
]