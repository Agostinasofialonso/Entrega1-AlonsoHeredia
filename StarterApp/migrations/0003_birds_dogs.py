# Generated by Django 4.2.2 on 2023-07-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarterApp', '0002_rename_name_cats_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]