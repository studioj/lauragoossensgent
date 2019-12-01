
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def bereikbaarheid(request):
    return render(request, 'bereikbaarheid.html')


def achtergrond(request):
    return render(request, 'achtergrond.html')