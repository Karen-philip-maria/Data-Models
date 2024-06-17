# Generated by Django 4.2.13 on 2024-06-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('code', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('country', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('immediate_contact', models.DateField(max_length=20)),
                ('bio', models.TimeField()),
            ],
        ),
    ]