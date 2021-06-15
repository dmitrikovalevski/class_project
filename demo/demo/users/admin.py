from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

