from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def help(request):
    pass


def get_started(request):
    pass
