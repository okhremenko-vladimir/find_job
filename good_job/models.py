from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='Название')
    location = models.CharField(max_length=32, verbose_name='Город')
    logo = models.ImageField(upload_to='logo/company/', default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField(verbose_name='Число сотрудников')
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    def amount_vacancies(self):
        return len(Vacancy.objects.filter(company__company_id=self.company_id))

    class Meta:
        verbose_name_plural = 'Компании'
        verbose_name = 'компанию'
        ordering = ['-employee_count']


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='logo/specialty/', default='https://place-hold.it/100x60')

    def __str__(self):
        return self.title

    def amount_vacancies(self):
        return len(Vacancy.objects.filter(specialty__code=self.code))


class Vacancy(models.Model):
    vacancy_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='Название')
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name="vacancies",
        verbose_name='Специализация',
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies", verbose_name='Компания')
    skills = models.CharField(max_length=128, verbose_name='Навыки')
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(verbose_name='Опубликовано')

    def skills_through_point(self):
        return ' • '.join(self.skills.split(', '))

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'вакансию'
        ordering = ['-published_at']


class Application(models.Model):
    written_username = models.CharField(max_length=64, verbose_name='Вас зовут')
    written_phone = PhoneNumberField(verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'заявку'
        ordering = ['-published']
