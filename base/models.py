from django.db import models
# Create your models here.

class Articles(models.Model): #Создаем модель (своего рода словарь) где ключи это переменные, а тип все что после равно это в каком формате мы принимем значения
    FirstName = models.CharField('Имя',max_length=50)
    SurName = models.CharField('Фамилия',max_length=50)
    Number = models.CharField('Номер Телефона',max_length=20)
    Age = models.IntegerField('Возраст')
    NameClub = models.CharField('Клуб',max_length=50,blank=True)
    NameNews = models.CharField('Событие',max_length=50,blank=True)
    University = models.CharField('Университет',max_length=50,blank=True)
    
    def __str__(self):
        return self.FirstName
    
    class Meta: 
        verbose_name="Участник" 
        verbose_name_plural="Участники" 