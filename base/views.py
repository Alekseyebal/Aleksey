from django.shortcuts import render, redirect
from .models import Articles
from main.models import Post
from datetime import datetime

from .forms import ArticlesForm
from django.views.generic import DeleteView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


# Create your views here.
def news_home(request): 
    news=Articles.objects.all() #Присваиваем перменной news массив из ВСЕХ словарей  Articles
    return render(request, 'base/data.html', {"news":news}) 


class DeleteBaseData(DeleteView):
    model = Articles
    success_url='/base'
    template_name='base/data.html'



def register(request, id):
    detail = Post.objects.get(pk=id)

    if request.method == "POST": 
        form = ArticlesForm(request.POST)
    
        
        if form.is_valid():
            article = form.save(commit=False)  # Не сохраняем пока в базе, чтобы изменить поля
            
            # Заполняем поля NameClub и NameNews из объекта detail
            article.NameClub = detail.ClubName
            article.NameNews = detail.NewsName
            
            # Сохраняем объект в базе данных
            article.save()
            
            return redirect('home')
    else:
        form=ArticlesForm()
    
    data={
         'form':form ,
         'detail':detail
    }
    return render(request, 'base/Register2.html',data)



class PostRegDetailView(DetailView):   
    model=Post
    template_name = 'base/Register2.html'
    context_object_name = 'reg'