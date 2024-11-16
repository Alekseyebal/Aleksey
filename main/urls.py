from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.PostNews, name="home"),
    path('<int:pk>', views.NewsDetailView.as_view(), name="news_datail"),
    path('search/', views.search_view, name='search'),
    path('about', views.about, name='about')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
