from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# TemplateView отобразит html страничку (контент не покажет)
# ListView отобразит и страничку и контент
# DetailView работает исключительно с id модели
# CreateView необходим для создания формы
#   form - переменная класса модели
#   as_p - каждое поле оборачивает в тег <p>
# UpdateView редактирует имеющуюся модель в базе данных
# DeleteView удаляет созданную модель из БД

from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'service/home.html'
    context_object_name = 'service'


class AboutTemplateView(TemplateView):
    template_name = 'service/about.html'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/post_detail.html'


class BlogCreateView(CreateView):
    model = Service
    template_name = 'service/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Service
    fields = ['name', 'category', 'description', 'price', 'photo']
    template_name = 'service/post_edit.html'



class BlogDeleteView(DeleteView):
    model = Service
    template_name = 'service/post_delete.html'
    success_url = reverse_lazy('home')
