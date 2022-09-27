from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError, Http404
from django.shortcuts import render

from .forms import ApplicationForm
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
    try:
        vacancy = Vacancy.objects.get(vacancy_id=vacancy_id)
    except Vacancy.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance_form = form.save(commit=False)
            instance_form.user = request.user
            instance_form.vacancy = vacancy
            instance_form.save()
            return HttpResponseRedirect('sent')
    else:
        form = ApplicationForm()
    form = ApplicationForm()
    context = {'vacancy': vacancy, 'form': form}
    return render(request, 'good_job/vacancy.html', context)


def search_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        found_vacancies = Vacancy.objects.filter(Q(title__icontains=search_query) | Q(skills__icontains=search_query))
    else:
        found_vacancies = Vacancy.objects.all()
    return render(request, 'good_job/search.html', {'vacancies': found_vacancies, 'search_query': search_query})


def sent_application_view(request, vacancy_id):
    return render(request, 'good_job/sent.html', {'vacancy_id': vacancy_id})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
