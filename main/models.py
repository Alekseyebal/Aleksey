from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Post(models.Model): #Создаем модель (своего рода словарь) где ключи это переменные, а тип все что после равно это в каком формате мы принимем значения
    ClubName= models.CharField('Название Клуба',max_length=50)
    NewsName = models.CharField('Название Новости',max_length=50)
    Anons = models.CharField('Анонс',max_length=250)
    TextNews=models.TextField('Статья')
    Date = models.DateTimeField("Дата события")
    Date_Stop = models.DateTimeField("Закрытие регистрации", default=datetime.now)
    ImgNews =  models.ImageField("Картинка Новости", blank = True, upload_to='main/image')
    
    def __str__(self):
        return self.ClubName
    
    class Meta: #Создаем название таблицы в странице алминистратора для нашей модели
        verbose_name="Новость" #Единичсное число
        verbose_name_plural="Новости" #Множественное число
