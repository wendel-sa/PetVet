# Generated by Django 4.0.4 on 2022-05-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_physicalexam_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalexam',
            name='choice_pain_m',
            field=models.CharField(choices=[('Não', 'Não'), ('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5')], max_length=3, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='linfonodos',
            field=models.CharField(max_length=60, verbose_name='Linfonodos'),
        ),
    ]
