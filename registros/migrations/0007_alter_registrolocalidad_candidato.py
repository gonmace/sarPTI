# Generated by Django 4.2.11 on 2024-04-18 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_alter_candidato_options_candidato_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrolocalidad',
            name='candidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.candidato', unique=True),
        ),
    ]
