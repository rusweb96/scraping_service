from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    query_set = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        query_set = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': query_set, 'form': form})
