from django.contrib import admin
from .models import Application, Company, Vacancy


class ApplicationAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'employee_count', 'owner',)
    list_display_links = ('name',)
    search_fields = ('name', 'location',)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'specialty', 'skills', 'company', 'published_at', )
    list_display_links = ('title',)
    search_fields = ('title', 'company', 'specialty',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
