from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    context = {}
    return render(request, 'good_job/index.html', context)


def vacancies_view(request):
    context = {}
    return render(request, 'good_job/vacancies.html', context)


def vacancies_cat_view(request, speciality):
    context = {}
    return render(request, 'good_job/vacancies_cat.html', context)


def company_view(request, company_id):
    context = {}
    return render(request, 'good_job/company.html', context)


def vacancy_view(request, vacancy_id):
    context = {}
    return render(request, 'good_job/vacancy.html', context)
