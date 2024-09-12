from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.


@login_required(login_url='dashboard:sign_in')
def index(request):
    return render(request, 'dashboard.html')


