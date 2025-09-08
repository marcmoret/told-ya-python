from django.shortcuts import render

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
    context = {}
    return render(request, 'argument/user.html', context)