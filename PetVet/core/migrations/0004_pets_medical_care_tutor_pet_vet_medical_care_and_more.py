# Generated by Django 4.0.3 on 2022-03-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_medicalcare_tutor_vet_alter_pets_breed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='medical_care',
            field=models.ManyToManyField(help_text='Escolha um atendimento', to='core.medicalcare'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='pet',
            field=models.ManyToManyField(help_text='Selecione um pet', to='core.pets'),
        ),
        migrations.AddField(
            model_name='vet',
            name='medical_care',
            field=models.ManyToManyField(help_text='Escolha um atendimento', to='core.medicalcare'),
        ),
        migrations.AlterField(
            model_name='medicalcare',
            name='sedative',
            field=models.CharField(blank=True, choices=[('N', 'Nao'), ('S', 'Simples'), ('C', 'Complexo')], default='N', help_text='Escolha o tipo de sedativo', max_length=1),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='district',
            field=models.CharField(help_text='Digite o Bairro', max_length=40),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='state',
            field=models.CharField(help_text='Digite o Estado', max_length=40),
        ),
    ]