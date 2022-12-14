# Generated by Django 4.1.2 on 2022-10-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')])),
                ('data_nasc', models.DateField()),
                ('telefone', models.CharField(max_length=25)),
                ('tipo', models.IntegerField(choices=[(1, 'Pessoa Ficica'), (2, 'Pessoa Juridica')])),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.endereco')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
