# Generated by Django 3.1.2 on 2020-11-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cli', models.CharField(max_length=200)),
                ('rut_cli', models.CharField(max_length=9)),
            ],
        ),
    ]
