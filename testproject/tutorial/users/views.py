# Отобразить страницу и вернутся в указанное место
from django.shortcuts import render, redirect
# Форма для регистрации пользователя
from .forms import NewUserForm, UpdateProfileForm, UpdateUserForm
# Одноразовые сообщения
from django.contrib import messages
# "Ключи" для аутентификации, входа в систему, выхода из системы
from django.contrib.auth import authenticate, login, logout
# Декораторы
from .decorators import unauthenticated_user, for_group_only
# Гпуппы. Необходимы для автоматического добавления пользователя в группу при регистрации
from django.contrib.auth.models import Group
# Для зависимости с картинкой
from .models import UserAccount
# Класс для смены пароля. Посленяя страница.
from django.contrib.auth.views import PasswordResetCompleteView


@for_group_only(group_list=['user'])
def user_account(request):
    service = request.user.service_set.all()
    # Добавляем очередь в контекст и выводим в шаблоне
    context = {
        'all_services': service
    }
    return render(request, 'users/profile.html', context)


@unauthenticated_user
def create_user(request):
    # Выведем на экран форму для заполнения регистрации пользователя
    new_user = NewUserForm()
    # Из формы в шаблоне к нам придут переменные с именем, емейлом и паролями
    if request.method == 'POST':
        # Принимаем переменные и подставляем их в форму для создания пользователя
        new_user = NewUserForm(request.POST)
        # Прверка на валидность формы.
        if new_user.is_valid():
            # Если форма корректна, тогда сохраним её
            user = new_user.save()
            # Получим группу из спика доступных групп из админки
            group = Group.objects.get(name='user')
            # Добавим группу пользователю
            user.groups.add(group)
            # При создании пользователя явно указываем на его зависимость с картинкой
            # Говоря что заполненая форма модели юзера передаётся в класс с картинкой.
            # Передаётся в поле user = models.ForeingKey(User)
            UserAccount.objects.create(user=user)
            # Так же после успешной регситрации сработает наше одноразовое сообщение.
            # Его можно передать в любой шалон. В данном случае после регистрации мы перейдём
            # на страницу входа и там, ниже мы увидим данное сообщение.
            # Своего рода такой тригер, если сохранили форму, дай нам сообщение и пока там где скажу.
            messages.success(request,
                             # new_user.cleaned_data.get('username') один из многих методов получить информацию
                             # для сообщения.
                             'Пользователь ' + new_user.cleaned_data.get('username') + ' успешно зарегистриван!')
            return redirect('login')

    context = {
        'form': new_user,
    }
    return render(request, 'users/registration.html', context)


@unauthenticated_user
def login_user(request):
    # Метод пост отправляет данные из формы с шаблона сайта
    if request.method == 'POST':
        # Запросе который пришел в методе ПОСТ есть переменные из полей ввода
        # Поле ввода ника
        username = request.POST.get('username')
        # Поле ввода пароля
        password = request.POST.get('password')
        # Проверка авторизации пользователя.
        # Проверка аутентификации. Проверяет есть ли пользователь в базе данных
        user = authenticate(request, username=username, password=password)
        # Пустая форма всегда присылает None
        # Если форма не пустая, тогда пользователь входит в систему
        if user is not None:
            # Уже в форму django подставляются наши проверенные ник и пароль
            login(request, user)
            # Перенавправляет на указанную страницу
            return redirect('/')
        else:
            # Если форма заполнена не верно, получим сообщение и вернёмся к форме
            messages.info(request, 'Неверно ввдён логин или пароль')
    return render(request, 'users/login.html')


def logout_user(request):
    # Эта функция из django которая позволяет выйти из аккаунта
    logout(request)
    return redirect('login')


def update_account(request):
    if request.method == 'POST':
        form1 = UpdateProfileForm(request.POST, request.FILES, instance=request.user.useraccount)
        if form1.is_valid():
            form1.save()
        form2 = UpdateUserForm(request.POST, instance=request.user)
        if form2.is_valid():
            form2.save()
        return redirect('account')
    form = UpdateProfileForm(instance=request.user.useraccount)
    user = UpdateUserForm(instance=request.user)

    context = {
        'userform': user,
        'form': form,
    }
    return render(request, 'users/update.html', context)


class ChangePasswordP4(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
