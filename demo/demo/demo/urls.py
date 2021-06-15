"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    # Очень важна последовательность данных путей на ссылки приложений
    # В особенности с пользователями
    # !!!  ВАЖНО  !!!
    # Если мы сделаем запрос accounts/any_path django сначала проверит 'django.contrib.auth.urls'
    # а затем уже приложение с юзерами 'users.urls'

    # В главе 9 указано сделать замену. Далее указан код как было:
    path('', include('service.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # path('', TemplateView.as_view(template_name='service/home.html'), name='home'),
    # path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # path('service/', include('service.urls')),
]

