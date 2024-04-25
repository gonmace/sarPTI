# Generated by Django 4.2.11 on 2024-04-22 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registros", "0003_registrollegada"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registrollegada",
            options={
                "verbose_name": "Registro Llegada",
                "verbose_name_plural": "Registro Llegadas",
            },
        ),
        migrations.CreateModel(
            name="RegistroLocalidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provincia", models.CharField(blank=True, max_length=25, null=True)),
                ("municipio", models.CharField(blank=True, max_length=25, null=True)),
                ("localidad", models.CharField(blank=True, max_length=25, null=True)),
                ("energia_localidad", models.BooleanField(default=True)),
                (
                    "candidato",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registros.candidato",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro Localidad",
                "verbose_name_plural": "Registro Localidades",
            },
        ),
    ]
