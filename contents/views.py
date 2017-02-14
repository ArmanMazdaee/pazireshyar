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


class Program(DetailView):
    template_name = 'contents/program.html'
    model = models.Program


def programs(request):
    countries = (models.University.objects.order_by().values('country').
                 distinct())
    countries = [country['country'] for country in countries]
    countries.append('')

    input_q = request.GET.get('q', '')
    input_country = request.GET.get('country', '')
    input_degree = request.GET.get('degree', '')
    input_toefl = request.GET.get('toefl', '')

    search = {}
    if input_q != '':
        search['name__contains'] = input_q
    if input_country != '':
        search['university__country'] = input_country
    if input_degree != '':
        search['degree'] = input_degree
    if input_toefl != '':
        search['minimum_toefl__gte'] = input_toefl
    programs = models.Program.objects.filter(**search)

    context = {
        'input_q': input_q,
        'input_country': input_country,
        'input_degree': input_degree,
        'input_toefl': input_toefl,
        'countries': countries,
        'programs': programs,
    }

    return render(request, 'contents/programs.html', context)
