# Generated by Django 4.2.11 on 2024-04-18 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0010_registropropietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propiedad_rol', models.CharField(max_length=100)),
                ('propiedad_escritura', models.CharField(max_length=100, verbose_name='Escritura')),
                ('propiedad_registro_civil', models.TextField(max_length=100, verbose_name='Registro Civil')),
                ('propiedad_imagen', models.ImageField(blank=True, null=True, upload_to='sitios/')),
                ('propiedad_descripcion', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('candidato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registros.candidato')),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
            },
        ),
    ]
