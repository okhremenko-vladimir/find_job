from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from good_job.views import company_view, main_view, vacancies_cat_view, vacancies_view, vacancy_view

urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:speciality>/', vacancies_cat_view, name='vacancies_cat'),
    path('company/<int:company_id>/', company_view, name='company'),
    path('vacancy/<int:vacancy_id>/', vacancy_view, name='vacancy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
