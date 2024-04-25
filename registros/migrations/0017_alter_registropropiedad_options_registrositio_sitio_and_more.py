# Generated by Django 4.2.11 on 2024-04-22 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registros", "0016_registropropiedad_sitio_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registropropiedad",
            options={
                "verbose_name": "Registro Propiedad",
                "verbose_name_plural": "Registros Propiedades",
            },
        ),
        migrations.AddField(
            model_name="registrositio",
            name="sitio",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="registros.sitio",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="registrositio",
            name="candidato",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="registros.candidato",
            ),
        ),
    ]
