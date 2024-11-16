from .models import Articles
from django.forms import ModelForm, TextInput
from django import forms


class ArticlesForm(ModelForm): #Создаем тип форм которые принимают значения в виде модели Articles 
    UNIVERSITY_CHOICES = [
        ('', 'Выберите университет'),
        ('Almau', 'Almau'),
        ('КазНу', 'КазНу'),
        ('KAU', 'KAU'),
        ('МУИТ', 'МУИТ'),
    ]

    University = forms.ChoiceField(
        choices=UNIVERSITY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form',
        }),
        label="Выберите университет"
    )
    
    class Meta:
        model=Articles
        fields=['FirstName','SurName','Number','Age','NameClub','NameNews', 'University']
        
        widgets={ 
              "FirstName": TextInput(attrs={
                'class':"form",
                'placeholder':"Имя"
              }),
              "SurName": TextInput(attrs={
                'class':"form",
                'placeholder':"Фамилия"
              }),
              "Number": TextInput(attrs={
                'class':"form",
                'placeholder':"+7 (***) *** ** **"
              }),
              "Age": TextInput(attrs={
                'class':"form",
                'placeholder':"Возраст"
              }),   
              
        }
        
    