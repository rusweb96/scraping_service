from django.shortcuts import render

from .models import Vacancy


def home_view(request):
    query_set = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'object_list': query_set})
