from django.contrib import admin

# Register your models here.

from .models import Articles

admin.site.register(Articles) #на стрице администратора будут отображаться данные Articles