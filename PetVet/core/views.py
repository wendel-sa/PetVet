from .models import MedicalCare, Pets, Tutor, Vet, GeneralClinic, PhysicalExam
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, TemplateView


# Views Index
class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        num_pets = Pets.objects.all().count()
        num_tutors = Tutor.objects.all().count()
        num_medical_cares = MedicalCare.objects.all().count()

        context['num_pets'] = num_pets
        context['num_tutors'] = num_tutors
        context['num_medical_cares'] = num_medical_cares

        return context


# Views Medical Care
class MedicalCareList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    template_name = 'core/medical_care_list.html'


class MedicalCareDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    template_name = 'core/medicalcare_detail.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo atendimento.'

        return context


class MedicalCareUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse atendimento.'

        return context


class MedicalCareDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = MedicalCare
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('medical_cares')


# Views Pet
class PetList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pets
    template_name = 'core/pet_list.html'


class PetDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Pets
    template_name = 'core/pet_detail.html'
    success_url = reverse_lazy('pets')


class PetCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('pets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class PetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('pets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class PetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = Pets
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('pets')


# Views Tutor
class TutorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tutor
    template_name = 'core/tutor_list.html'


class TutorDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Tutor
    template_name = 'core/tutor_detail.html'
    success_url = reverse_lazy('tutors')


class TutorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('tutors')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class TutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('tutors')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class TutorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = Tutor
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('tutors')


# Views Vet
class VetList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Vet
    template_name = 'core/vet_list.html'


class VetCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('vets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class VetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('vets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class VetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = Vet
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('vets')


# Views General Clinic
class GeneralClinicCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = GeneralClinic
    fields = ['medical_care', 'choice_anamnese',
              'anamnese', 'choice_anti_rabica', 'choice_type_v', 'choice_v', 'choice_type_felina', 'choice_felina', 'others_felina', 'choice_verminose', 'others_verminose', 'choice_ectopas', 'others_ectopas', 'choice_leish']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Ficha Clínica Geral'
        context['title_page'] = 'Ficha Clínica Geral'
        context['tips'] = 'Preencha os campos para criar uma nova ficha de clínica geral.'

        return context


# Views Physical Exam
class PhysicalExamCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = PhysicalExam
    fields = ['medical_care', 'choice_conduct',
              'weight', 'choice_consciousness', 'stance', 'hydration', 'choice_nutricional_status', 'oculopalpebral', 'bucal', 'genital', 'choice_dental_calculus', 'choice_dental_loss', 'gengivite', 'choice_ulcera', 'choice_halitose', 'linfonodos', 'fc', 'fr', 'tpc', 'tr', 'pulse', 'choice_auscu_cardio', 'heart_rate']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Exame Fisico Geral'
        context['title_page'] = 'Exame Fisico Geral'
        context['tips'] = 'Preencha os campos para criar um novo exame fisico geral.'

        return context
