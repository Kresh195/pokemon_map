# Generated by Django 3.1.14 on 2025-07-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_pokemon_ru_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='Ru_Name',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='Name_Ru',
            field=models.CharField(default='Покемон', max_length=200),
        ),
    ]
