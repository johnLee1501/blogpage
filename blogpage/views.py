from django.shortcuts import render, redirect

from blogpage.forms import CommentForm
from blogpage.models import Post, Category


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blogpage/frontpage.html', {'posts': posts})


def detail(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.save()

            return redirect('detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blogpage/detail.html', {'post': post, 'form': form})


def category(request, id):
    category = Category.objects.get(id=id)

    return render(request, 'blogpage/category.html', {'category': category})
