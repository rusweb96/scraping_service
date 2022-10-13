from django.shortcuts import render

import datetime


def home(request):
    name = 'Руся'
    date = datetime.datetime.now().date()
    context = {'name': name, 'data': date}
    return render(request, 'home.html', context)