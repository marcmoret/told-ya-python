from django.shortcuts import render

from .models import *

# Create your views here.

def main(request):
    context = {}
    return render(request, 'argument/main.html', context)

def voting(request):
    context = {}
    return render(request, 'argument/voting.html', context)

def phone_input(request):
    context = {}
    return render(request, 'argument/phone-input.html', context)

def user(request):
    users = User.objects.all()  # Get all users
    context = {'users': users}
    return render(request, 'argument/user.html', context)

def home(request):
    context = {}
    return render(request, 'argument/home.html', context)

def argument(request):
    context = {}
    return render(request, 'argument/argument.html', context)