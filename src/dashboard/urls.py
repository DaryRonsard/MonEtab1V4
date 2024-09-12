from django.urls import path
from dashboard.views import index
from user.views.user_views import connexion, disconnect


app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('sign_in/', connexion, name='sign_in'),
    path('logout/', disconnect, name='logout'),
]