from django.views.generic import DetailView
from django.shortcuts import render

from . import models


class University(DetailView):
    template_name = 'contents/university.html'
    model = models.University


def universities(request):
    countries = (models.University.objects.order_by().values('country').
                 distinct())
    countries = [country['country'] for country in countries]
    countries.append('')

    input_country = request.GET.get('country', '')
    input_q = request.GET.get('q', '')

    universities = models.University.objects.all()
    if input_q != '':
        universities = universities.filter(name__contains=input_q)
    if input_country != '':
        universities = universities.filter(country=input_country)

    context = {
        'input_q': input_q,
        'input_country': input_country,
        'countries': countries,
        'universities': universities,
    }
    return render(request, 'contents/universities.html', context)


class Field(DetailView):
    template_name = 'contents/field.html'
    model = models.Field


def fields(request):
    input_q = request.GET.get('q', '')

    search = {}
    if input_q != '':
        search['name__contains'] = input_q
    fields = models.Field.objects.filter(**search)

    context = {
        'input_q': input_q,
        'fields': fields,
    }

    return render(request, 'contents/fields.html', context)
