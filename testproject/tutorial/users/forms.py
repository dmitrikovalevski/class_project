# Готовая django для создания пользователя
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Готовая модель пользователя на которой построится форма
from django.contrib.auth.models import User
# Форима для редактирования формы пользователя
from django import forms
#
from .models import UserAccount


# Класс формы
class NewUserForm(UserCreationForm):
    class Meta:
        # Модель пользователя
        model = User
        # Поля из модели которые будут использованы при регистрации
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['picture']
