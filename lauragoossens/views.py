from django.shortcuts import render


def index(request):
    context = {"page_title": "index"}
    return render(request, 'index.html', context)


def contact(request):
    context = {"page_title": "contact"}
    return render(request, 'contact.html', context)


def bereikbaarheid(request):
    context = {"page_title": "bereikbaarheid"}
    return render(request, 'bereikbaarheid.html', context)


def achtergrond(request):
    context = {"page_title": "achtergrond"}
    return render(request, 'achtergrond.html', context)
