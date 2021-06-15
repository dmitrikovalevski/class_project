from .models import Service, Comments
from .forms import CommentsForm
from django.contrib.auth.models import User

from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView, FormMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,
                                  )


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'service/all_services.html'


class ServiceDetailView(DetailView, CreateView):
    model = Service
    context_object_name = 'service'
    template_name = 'service/service_id.html'
    form_class = CommentsForm

    # Get Service count
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_user = Service.objects.get(pk=self.kwargs['pk']).user
        if not self.request.user == service_user:
            print(self.request.user, service_user)
            service = Service.objects.get(pk=self.kwargs['pk'])
            service.count += 1
            service.save()
        context['count'] = Service.objects.get(pk=self.kwargs['pk']).count
        return context

    # Comment form
    def form_valid(self, form):
        comment = form.save()
        if self.request.user.is_authenticated:
            comment.user = self.request.user
            comment.service = Service.objects.get(pk=self.kwargs['pk'])
            comment.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('detail', self.kwargs['pk'])


class ServiceCreateView(CreateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/add_service.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        service = form.save(commit=False)
        if self.request.user.is_authenticated:
            service.user = self.request.user
            service.save()
        return redirect(self.get_success_url())


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/update_service.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/delete_service.html'
    success_url = 'home'

    def get_success_url(self):
        return reverse('home')
