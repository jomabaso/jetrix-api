# Generated by Django 4.2.16 on 2024-11-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_tablero', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
