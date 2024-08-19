from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "login.html")


@login_required
def home(request):
    return render(request, "home.html")
