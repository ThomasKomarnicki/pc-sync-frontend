from django.shortcuts import render
from .models import Faq


def home(request):
    return render(request, 'home.html')


def help(request):
    # faq = Faq.objects.order_by('order').all()
    sections = [
        {
            'title': 'Connection',
            'items': [
                {'question': 'Why is the app never able to connect to my computer?',
                 'answer': 'Make sure your Android TV and Windows PC are on the same local network'},
            ]
        },
        {
            'title': 'Android App',
            'items': [

                {'question': 'Why is there a black screen when I try to play some videos?',
                 'answer': 'These videos may be improperly encoded and therefore not playable'},
            ]
        },
        {
            'title': 'Windows App',
            'items': [

            ]
        },
    ]

    # for qa in faq:
    #     items.append({'question': qa.question, 'answer': qa.answer})

    return render(request, 'help.html', context={'faq': sections})


def get_started(request):
    return render(request, 'get_started.html')


def download(request):
    return render(request, 'download.html')
