from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def help(request):
    return render(request, 'help.html')


def get_started(request):
    return render(request, 'get_started.html')


def download(request):
    return render(request, 'download.html')
