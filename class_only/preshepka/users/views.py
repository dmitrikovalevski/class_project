from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView
from .forms import CreateUserForm, UserAccountUpdateForm
from .models import UserInfo
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group


class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    # add user for group
    def form_valid(self, form):
        user = form.save()
        if Group.objects.get(name='user'):
            user.groups.add(Group.objects.get(name='user').pk)
            user.save()
            return super().form_valid(form)
        else:
            group = Group.objects.create(name='user')
            user.groups.add(group)
            user.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class UserLogIn(LoginView):
    pass


class UserLogOut(LogoutView):
    pass


class UserAccountView(DetailView):
    model = User
    template_name = 'users/account_detail.html'


def update_user_account(request):
    # update user profile
    if request.method == 'POST':
        form = UserAccountUpdateForm(request.POST, request.FILES,
                                     instance=request.user.userinfo)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.save()
            return redirect('account', request.user.id)
    else:
        form = UserAccountUpdateForm(instance=request.user.userinfo)
    context = {
        'form': form
    }
    return render(request, 'users/account_update.html', context)


# reset password
class PasswordReset(PasswordResetView):
    pass


class PasswordResetConfirm(PasswordResetConfirmView):
    pass


class PasswordResetDone(PasswordResetDoneView):
    pass


class PasswordResetComplete(PasswordResetCompleteView):
    pass
