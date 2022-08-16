from django.db import models


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='company_logo/', default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def amount_vacancies(self):
        return len(Vacancy.objects.filter(company__company_id=self.company_id))


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='specialty_logo/', default='https://place-hold.it/100x60')

    def amount_vacancies(self):
        return len(Vacancy.objects.filter(specialty__code=self.code))


class Vacancy(models.Model):
    vacancy_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=128)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def skills_through_point(self):
        return ' • '.join(self.skills.split(', '))
