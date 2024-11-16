from django.urls import path
from . import views


 #Ссылки на функции в views через url строку (также мы даем название для ссылки для более удобного перемещения в дльнейшем)
urlpatterns = [
    path('',views.news_home, name="news_home"),
    path('<int:pk>', views.PostRegDetailView.as_view(), name="reg_datail"),
    path('register/<int:id>/', views.register, name="register")  
]

