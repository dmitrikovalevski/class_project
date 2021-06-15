from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return inner


def for_group_only(group_list=[]):
    def decorator(view_func):
        def inner(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in group_list:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('У вас нету доступа к этой функции')

        return inner

    return decorator


def admin_only(view_func):
    def inner(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('У вас нету доступа к этой функции')

    return inner
