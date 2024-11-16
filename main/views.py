from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import DetailView
from .forms import SearchForm
from django.utils import timezone




def about(request):
    return render(request,'main/Post.html')

def PostNews(request):
    PostNews = Post.objects.order_by('Date')
    return render(request,'main/Glavnaya.html', {"PostNews":PostNews})

class NewsDetailView(DetailView):
    model=Post
    template_name = 'main/Post.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Получаем стандартный контекст
        context['date_now'] = timezone.now()  # Добавляем текущую дату в контекст
        return context



def search_view(request):
    query = request.GET.get('query', '')
    postnews = Post.objects.filter(ClubName__icontains=query) if query else Post.objects.none()

    return render(request, 'main/search.html', {'PostNews': postnews, 'query': query})


