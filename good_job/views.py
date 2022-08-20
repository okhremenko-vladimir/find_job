from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from .models import Vacancy, Company, Specialty


def main_view(request):
    specialties = Specialty.objects.all()
    companies = Company.objects.all()
    context = {'specialties': specialties, 'companies': companies}
    return render(request, 'good_job/index.html', context)


def vacancies_view(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies, 'speciality': 'all'}
    return render(request, 'good_job/vacancies.html', context)


def vacancies_cat_view(request, speciality):
    vacancies_by_speciality = Vacancy.objects.filter(specialty__code=speciality)
    context = {'speciality': speciality, 'vacancies': vacancies_by_speciality}
    return render(request, 'good_job/vacancies.html', context)


def company_view(request, company_id):
    company = Company.objects.get(company_id=company_id)
    vacancies = Vacancy.objects.filter(company=company_id)
    context = {'company': company, 'vacancies': vacancies}
    return render(request, 'good_job/company.html', context)


def vacancy_view(request, vacancy_id):
    vacancy = Vacancy.objects.get(vacancy_id=vacancy_id)
    context = {'vacancy': vacancy}
    return render(request, 'good_job/vacancy.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
