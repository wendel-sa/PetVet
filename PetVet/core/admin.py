from core.models import MedicalCare, Pets, Tutor, Vet
from django.contrib import admin

# admin.site.register(MedicalCare)
# admin.site.register(Pets)
# admin.site.register(Tutor)
admin.site.register(Vet)


class MedicalCareAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'procedure', 'sedative', 'report')


admin.site.register(MedicalCare, MedicalCareAdmin)


class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet_name', 'species', 'breed',
                    'gender', 'date_of_birth', 'castrated', 'weight')


admin.site.register(Pets, PetsAdmin)


class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_name', 'cpf', 'phone', 'email',
                    'street', 'number', 'district', 'state', 'cep')


admin.site.register(Tutor, TutorAdmin)
