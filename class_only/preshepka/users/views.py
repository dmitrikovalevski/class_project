from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView,\
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CreateUserForm


class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    def get_success_url(self):
        return reverse('home')


class UserLogIn(LoginView):
    pass


class UserLogOut(LogoutView):
    pass


class UserAccountListView(ListView):
    model = User
    template_name = 'users/account.html'


class UserAccountUpdate(UpdateView):
    pass


# reset password
class PasswordReset(PasswordResetView):
    pass


class PasswordResetConfirm(PasswordResetConfirmView):
    pass


class PasswordResetDone(PasswordResetDoneView):
    pass


class PasswordResetComplete(PasswordResetCompleteView):
    pass



