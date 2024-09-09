from django.urls import path
from report.views import index
#from user.views.user_views import index,register_user,login_user


app_name = 'report'
urlpatterns = [
    path('', index, name='index'),
]
