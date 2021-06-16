from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserInfo


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserAccountUpdateForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ['image', 'phone']
