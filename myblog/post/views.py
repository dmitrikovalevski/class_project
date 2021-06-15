from django.shortcuts import render, redirect

# Модели
from .models import Post, Img
# Формы
from .forms import PostForm


def home(request):
    post = Post.objects.order_by()
    context = {
        'post': post
    }
    return render(request, 'post/home.html', context)


def get_post(request, id):
    post = Post.objects.get(pk=id)
    img = Img.objects.get(pk=1)
    context = {
        'post': post,
        'img': img,
    }
    return render(request, 'post/post_id.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'post/add_post.html', {'form': form})


def edit_post(request, id):
    p = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'post/edit_post.html', {'form': form})


def delete_post(request, id):
    p = Post.objects.get(pk=id)
    p.delete()

    return redirect('/')

