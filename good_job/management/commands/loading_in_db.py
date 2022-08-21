from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date

from good_job.data import jobs, companies, specialties
from good_job.models import Vacancy, Company, Specialty


class Command(BaseCommand):

    def handle(self, *args, **options):
        for company in companies:
            User.objects.create_user(
                username=company['title'] + '_user',
                email=company['title'] + '@example.com',
                password=company['employee_count'] + company['title']
            )
            row = Company(
                company_id=int(company['id']),
                name=company['title'],
                location=company['location'],
                logo='logo/company/' + company['logo'],
                description=company['description'],
                employee_count=company['employee_count'],
                owner=User.objects.get(username=company['title'] + '_user'),
            )
            row.save()
        for specialty in specialties:
            row = Specialty(
                code=specialty['code'],
                title=specialty['title'],
                picture='logo/specialty/' + specialty['picture']
            )
            row.save()
        for job in jobs:
            row = Vacancy(
                vacancy_id=int(job['id']),
                title=job['title'],
                specialty=Specialty.objects.get(code=job['specialty']),
                company=Company.objects.get(company_id=int(job['company'])),
                skills=job['skills'],
                description=job['description'],
                salary_min=int(job['salary_from']),
                salary_max=int(job['salary_to']),
                published_at=parse_date(job['posted']),
            )
            row.save()
