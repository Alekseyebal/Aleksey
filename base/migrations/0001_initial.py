# Generated by Django 4.2.16 on 2024-10-16 15:30

from django.db import migrations, models 



class Migration(migrations.Migration): #Автоматически созданная миграция на основе модели Articles

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, verbose_name='Имя')),
                ('SurName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('Number', models.CharField(max_length=15, verbose_name='Номер Телефона')),
                ('Age', models.IntegerField(max_length=2, verbose_name='Возраст')),
                #('NameClub', models.CharField(max_length=50, verbose_name='Клуб')),
                #('NameNews', models.CharField(max_length=50, verbose_name='Событие')),
            ],
        ),
    ]
