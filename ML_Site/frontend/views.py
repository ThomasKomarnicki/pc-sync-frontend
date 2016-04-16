from django.shortcuts import render
from .models import Faq


def home(request):
    return render(request, 'home.html')


def help(request):
    faq = Faq.objects.order_by('order').all()
    items = []
    for qa in faq:
        items.append({'question': qa.question, 'answer': qa.answer})

    return render(request, 'help.html', context={'faq': items})


def get_started(request):
    return render(request, 'get_started.html')


def download(request):
    return render(request, 'download.html')
